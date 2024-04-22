from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.common.converters.base import BaseConverter
from src.apps.vacancies.entities import VacancyEntity
from src.apps.vacancies.filters import VacancyFilters


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

    @abstractmethod
    def get(self, id: int) -> VacancyEntity:
        ...

    @abstractmethod
    def create(self, **vacancy_data) -> VacancyEntity:
        ...

    @abstractmethod
    def add_candidate(self, candidate_id: int) -> None:
        ...
