from dataclasses import dataclass

from django.db.models import Q

from src.apps.profiles.services.base import BaseEmployerService
from src.apps.vacancies.filters import VacancyFilters
from src.apps.vacancies.entities import VacancyEntity
from src.apps.vacancies.models import Vacancy

from .base import BaseVacancyService


@dataclass
class ORMVacancyService(BaseVacancyService):
    employer_service: BaseEmployerService

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

    def create(self, **vacancy_data) -> VacancyEntity:
        employer_model = self.employer_service.converter.handle(
            vacancy_data.pop('employer')
        )
        new_vacancy = Vacancy.objects.create(
            employer=employer_model,
            **vacancy_data,
        )
        return self.converter.handle(new_vacancy)

    def add_candidate(self, vacancy_id: int, candidate_id: int) -> None:
        ...
