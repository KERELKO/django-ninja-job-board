from dataclasses import dataclass

from django.db.models import Q

from src.common.services.base import BaseService
from src.common.converters.base import BaseConverter

from src.apps.vacancies.filters.vacancies import VacancyFilters
from src.apps.vacancies.converters.vacancies import ORMVacancyConverter
from src.apps.vacancies.entities.vacancies import Vacancy as VacancyEntity
from src.apps.vacancies.models.vacancies import Vacancy


@dataclass
class ORMVacancyService(BaseService):
    converter: BaseConverter = ORMVacancyConverter()

    def _build_queryset(self, filters: VacancyFilters) -> Q:
        query = Q(open=True)
        if filters.search is not None:
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
        return query

    def get_list(
        self,
        filters: VacancyFilters,
        offset: int = 0,
        limit: int = 20,
    ) -> list[VacancyEntity]:
        query = self._build_queryset(filters=filters)
        vacancy_list = Vacancy.objects.filter(query)[offset: offset + limit]
        return [self.converter.handle(vacancy) for vacancy in vacancy_list]

    def get_total_count(self, filters: VacancyFilters) -> int:
        query = self._build_queryset(filters=filters)
        vacancy_count = Vacancy.available.filter(query).count()
        return vacancy_count

    def get_by_id(self, id: int) -> VacancyEntity:
        vacancy = Vacancy.objects.get(id=id)
        return self.converter.handle(vacancy)
