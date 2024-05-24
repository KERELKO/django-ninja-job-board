from typing import Any, Iterable

from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.apps.vacancies.entities import VacancyEntity
from src.apps.vacancies.filters import VacancyFilters
from src.apps.vacancies.services.base import BaseVacancyService


class FakeVacancyService(BaseVacancyService):
    def __init__(self, vacancy: VacancyEntity) -> None:
        self.vacancies: list[VacancyEntity] = [vacancy]

    def get_all(self, filters: VacancyFilters) -> Iterable[VacancyEntity]:
        for vacancy in self.vacancies:
            yield vacancy

    def get_list(
        self,
        filters: VacancyFilters,
        offset: int = 0,
        limit: int = 20,
    ) -> list[VacancyEntity]:
        return self.vacancies[offset:limit]

    def get(self, id: int) -> VacancyEntity | None:
        for v in self.vacancies:
            if v.id == id:
                return v
        return None

    def get_total_count(self, filters: Any) -> int:
        return len(self.vacancies)

    def create(self, employer_id: int, entity: VacancyEntity) -> VacancyEntity:
        self.vacancies.append(entity)
        return entity

    def add_candidate(self, candidate_id: int, vacancy_id: int) -> None:
        for v in self.vacancies:
            if v.id == vacancy_id:
                v.interested_candidates.append(candidate_id)

    def get_list_candidates(
        self,
        vacancy_id: int,
        offset: int = 0,
        limit: int = 20,
    ) -> list[JobSeekerEntity]:
        for v in self.vacancies:
            if v.id == vacancy_id:
                return v.interested_candidates[offset:limit]
        return []
