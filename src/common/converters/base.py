from abc import ABC, abstractmethod

from src.apps.vacancies.entities.vacancies import Vacancy as VacancyEntity


class BaseConverter(ABC):
    @abstractmethod
    def handle(self):
        ...

    @abstractmethod
    def convert_to_entity(self) -> VacancyEntity:
        ...
