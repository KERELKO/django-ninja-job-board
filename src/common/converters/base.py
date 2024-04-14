from abc import ABC, abstractmethod
from typing import Any

from src.apps.vacancies.entities.vacancies import Vacancy as VacancyEntity


class BaseConverter(ABC):
    @abstractmethod
    def handle(self, obj: Any) -> Any | VacancyEntity:
        ...

    @abstractmethod
    def convert_to_entity(self, obj: Any) -> VacancyEntity:
        ...
