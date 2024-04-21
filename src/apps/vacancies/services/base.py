from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.common.converters.base import BaseConverter
from src.apps.vacancies.entities.vacancies import Vacancy as VacancyEntity
from src.apps.vacancies.filters.vacancies import VacancyFilters


@dataclass
class BaseVacancyService(ABC):
    converter: BaseConverter

    @abstractmethod
    def get_list(
        self,
        filters: VacancyFilters,
        offset: int,
        limit: int
    ) -> list[VacancyEntity]:
        ...

    @abstractmethod
    def get_total_count(self, filters) -> int:
        ...
