from dataclasses import dataclass
from typing import Iterable

from django.db.models import Q

from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.common.services.exceptions import ServiceException
from src.apps.profiles.services.jobseekers import ORMJobSeekerService
from src.apps.profiles.services.employers import ORMEmployerService
from src.apps.vacancies.filters import VacancyFilters
from src.apps.vacancies.entities import VacancyEntity
from src.apps.vacancies.models import Vacancy

from .base import BaseVacancyService


@dataclass
class ORMVacancyService(BaseVacancyService):
    employer_service: ORMEmployerService
    jobseeker_service: ORMJobSeekerService

    def _get_model_or_raise_exception(
        self,
        message: str = None,
        related: bool = False,
        **lookup_parameters,
    ) -> Vacancy:
        try:
            if related:
                vacancy = (
                    Vacancy.objects.select_related('employer')
                    .prefetch_related('interested_candidates')
                    .get(**lookup_parameters)
                )
            else:
                vacancy = Vacancy.objects.get(**lookup_parameters)
        except Vacancy.DoesNotExist:
            if not message:
                raise ServiceException(message='Vacancy not found')
            raise ServiceException(message=message)
        return vacancy

    def _build_queryset(self, filters: VacancyFilters) -> Q:
        query = Q(open=True)
        if filters.search:
            query &= Q(title__icontains=filters.search)
            query &= Q(description__icontains=filters.search)
        if filters.is_remote is not None:
            query &= Q(is_remote=filters.is_remote)
        if filters.required_experience__gte:
            query &= Q(required_experience__gte=filters.required_experience__gte)
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
        vacancy_list = Vacancy.objects.filter(query)[offset : offset + limit]
        return [self.converter.handle(vacancy) for vacancy in vacancy_list]

    def get_total_count(self, filters: VacancyFilters) -> int:
        query = self._build_queryset(filters=filters)
        vacancy_count = Vacancy.available.filter(query).count()
        return vacancy_count

    def get(self, id: int) -> VacancyEntity:
        vacancy = self._get_model_or_raise_exception(
            id=id,
            related=False,
            message=f"Vacancy with id '{id}' not found",
        )
        return self.converter.handle(vacancy)

    def get_all(self, filters: VacancyFilters) -> Iterable[VacancyEntity]:
        query = self._build_queryset(filters=filters)
        for vacancy in Vacancy.objects.filter(query):
            yield self.converter.handle(vacancy)

    def create(self, employer_id: int, **vacancy_data) -> VacancyEntity:
        employer = self.employer_service._get_model_or_raise_exception(
            id=employer_id
        )
        new_vacancy = Vacancy.objects.create(
            employer=employer,
            **vacancy_data,
        )
        return self.converter.handle(new_vacancy)

    def add_candidate(self, vacancy_id: int, candidate_id: int) -> None:
        candidate = self.jobseeker_service._get_model_or_raise_exception(
            id=candidate_id
        )
        vacancy = self._get_model_or_raise_exception(
            id=vacancy_id,
            message=f"Vacancy with id '{vacancy_id}' not found",
            related=True,
        )
        vacancy.interested_candidates.add(candidate.id)

    def get_list_candidates(
        self,
        vacancy_id: int,
        offset: int = 0,
        limit: int = 20,
    ) -> list[JobSeekerEntity]:
        vacancy = Vacancy.objects.get(id=vacancy_id)
        candidates = vacancy.interested_candidates.all()[offset:limit]
        return [self.jobseeker_service.converter.handle(c) for c in candidates]
