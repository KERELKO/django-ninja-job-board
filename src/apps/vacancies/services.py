from dataclasses import dataclass

from django.db.models import Q

from src.core.common.converters.converters import BaseConverter

from .filters import VacancyFilters
from .converters import ORMVacancyConverter
from .models import Vacancy
from .entities import Vacancy as VacancyEntity


@dataclass
class ORMVacancyService:
    converter: BaseConverter = ORMVacancyConverter()

    def _build_queryset(self, filters: VacancyFilters) -> Q:
        query = Q(open=True)
        if filters.search is not None:
            query &= (
                Q(title__icontains=filters.search) |
                Q(description__icontains=filters.search)
            )
        return query

    def get_vacancy_list(
        self,
        offset: int,
        limit: int,
        filters: VacancyFilters
    ) -> list[VacancyEntity]:
        query = self._build_queryset(filters=filters)
        vacancy_list = Vacancy.objects.filter(query)[offset: offset + limit]
        return [self.converter.convert_to_entity(vacancy) for vacancy in vacancy_list]

    def get_vacancy_count(self) -> int:
        vacancy_count = Vacancy.available.count()
        return vacancy_count
