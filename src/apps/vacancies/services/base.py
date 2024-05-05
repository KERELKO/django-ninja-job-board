from abc import abstractmethod
from dataclasses import dataclass

from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.apps.vacancies.entities import VacancyEntity
from src.common.services.base import BaseService
from src.common.converters.base import BaseConverter


@dataclass
class BaseVacancyService(BaseService):
    converter: BaseConverter

    @abstractmethod
    def create(self, employer_id: int, **vacancy_data) -> VacancyEntity: ...

    @abstractmethod
    def add_candidate(self, candidate_id: int, vacancy_id: int) -> None: ...

    @abstractmethod
    def filter_candidates(
        self,
        vacancy_id: int,
        offset: int,
        limit: int,
    ) -> list[JobSeekerEntity]: ...
