from abc import abstractmethod
from dataclasses import dataclass

from src.common.services.base import BaseService
from src.common.converters.base import BaseConverter
from src.apps.vacancies.entities import VacancyEntity


@dataclass
class BaseVacancyService(BaseService):
    converter: BaseConverter

    @abstractmethod
    def create(self, employer_id: int, **vacancy_data) -> VacancyEntity:
        ...

    @abstractmethod
    def add_candidate(self, candidate_id: int, vacancy_id: int) -> None:
        ...
