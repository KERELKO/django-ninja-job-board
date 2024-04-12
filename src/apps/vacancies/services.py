from dataclasses import dataclass

from src.apps.vacancies.converters import ORMVacancyConverter
from src.apps.vacancies.models import Vacancy
from src.core.common.converters.converters import BaseConverter

from .entities import Vacancy as VacancyEntity


@dataclass
class ORMVacancyService:
    converter: BaseConverter = ORMVacancyConverter()

    def get_vacancy_list(self) -> list[VacancyEntity]:
        vacancy_list = Vacancy.available.all()
        return [self.converter.convert_to_entity(vacancy) for vacancy in vacancy_list]

    def get_vacancy_count(self) -> int:
        vacancy_count = Vacancy.available.count()
        return vacancy_count
