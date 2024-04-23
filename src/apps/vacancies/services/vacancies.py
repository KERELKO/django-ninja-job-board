from dataclasses import dataclass
from typing import Iterable

from django.db.models import Q

from src.apps.profiles.models.employers import EmployerProfile
from src.apps.profiles.models.jobseekers import JobSeekerProfile
from src.apps.vacancies.filters import VacancyFilters
from src.apps.vacancies.entities import VacancyEntity
from src.apps.vacancies.models import Vacancy

from .base import BaseVacancyService


@dataclass
class ORMVacancyService(BaseVacancyService):

    def _build_queryset(self, filters: VacancyFilters) -> Q:
        query = Q(open=True)
        if filters.search:
            query &= (
                Q(title__icontains=filters.search) |
                Q(description__icontains=filters.search)
            )
        if filters.is_remote is not None:
            query &= Q(remote=filters.is_remote)
        if filters.required_experience__gte:
            query &= Q(
                required_experience__gte=filters.required_experience__gte
            )
        if filters.required_skills:
            # ?Icontains does not work with ArrayField
            skills = [skill.lower() for skill in filters.required_skills]
            query &= Q(required_skills__contains=skills)
        if filters.created_at__gte:
            query &= Q(created_at__gte=filters.created_at__gte)
        if filters.location:
            query &= Q(location=filters.location)
        if filters.company_name:
            query &= Q(company_name=filters.company_name)
        if filters.salary__gte:
            query &= Q(salary__gte=filters.salary__gte)
        if filters.salary__lte:
            query &= Q(salary__lte=filters.salary__lte)
        return query

    def get_list(
        self,
        filters: VacancyFilters,
        offset: int = 0,
        limit: int = 20,
    ) -> list[VacancyEntity]:
        query = self._build_queryset(filters=filters)
        vacancy_list = Vacancy.objects.filter(query)[offset:offset + limit]
        return [self.converter.handle(vacancy) for vacancy in vacancy_list]

    def get_total_count(self, filters: VacancyFilters) -> int:
        query = self._build_queryset(filters=filters)
        vacancy_count = Vacancy.available.filter(query).count()
        return vacancy_count

    def get(self, id: int) -> VacancyEntity:
        vacancy = Vacancy.objects.get(id=id)
        return self.converter.handle(vacancy)

    def get_all(self, filters: VacancyFilters) -> Iterable[VacancyEntity]:
        query = self._build_queryset(filters=filters)
        for vacancy in Vacancy.objects.filter(query):
            yield vacancy

    def create(
        self,
        employer_id: int,
        **vacancy_data,
    ) -> VacancyEntity:
        employer = EmployerProfile.objects.get(id=employer_id)
        new_vacancy = Vacancy.objects.create(
            employer=employer,
            **vacancy_data,
        )
        return self.converter.handle(new_vacancy)

    def add_candidate(self, vacancy_id: int, candidate_id: int) -> None:
        candidate = JobSeekerProfile.objects.get(id=candidate_id)
        vacancy = Vacancy.objects.get(id=vacancy_id)
        vacancy.interested_candidates.add(candidate.id)
