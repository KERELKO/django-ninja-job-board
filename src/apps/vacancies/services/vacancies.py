from dataclasses import dataclass

from django.db.models import Q

from src.common.services.base import BaseService
from src.common.converters.base import BaseConverter

from ..filters.vacancies import VacancyFilters
from ..converters.vacancies import ORMVacancyConverter
from ..entities.vacancies import Vacancy as VacancyEntity
from ..models.vacancies import Vacancy


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
        if filters.required_skills:
            ...
        if filters.remote is not None:
            query &= Q(remote=filters.remote)
        if filters.required_experience:
            query &= Q(required_experience__gte=filters.required_experience)
        return query

    def get_vacancy_list(
        self,
        offset: int,
        limit: int,
        filters: VacancyFilters
    ) -> list[VacancyEntity]:
        query = self._build_queryset(filters=filters)
        vacancy_list = Vacancy.objects.filter(query)[offset: offset + limit]
        return [self.converter.handle(vacancy) for vacancy in vacancy_list]

    def get_vacancy_count(self, filters: VacancyFilters) -> int:
        query = self._build_queryset(filters=filters)
        vacancy_count = Vacancy.available.filter(query).count()
        return vacancy_count

    def get_vacancy_by_id(self, id: int) -> VacancyEntity:
        vacancy = Vacancy.objects.get(id=id)
        return self.converter.handle(vacancy)
