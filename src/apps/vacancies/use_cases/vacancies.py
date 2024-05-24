from dataclasses import dataclass

from src.common.services.base import BaseNotificationService
from src.apps.profiles.filters import JobSeekerFilters
from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.apps.profiles.services.base import BaseJobSeekerService
from src.apps.vacancies.entities import VacancyEntity
from src.apps.vacancies.services.base import BaseVacancyService
from src.apps.vacancies.enums import VacancyCriteria


@dataclass
class CreateVacancyUseCase:
    vacancy_service: BaseVacancyService
    jobseeker_service: BaseJobSeekerService
    notification_service: BaseNotificationService

    def execute(
        self,
        employer_id: int,
        entity: VacancyEntity,
    ) -> VacancyEntity:
        new_vacancy = self.vacancy_service.create(
            entity=entity, employer_id=employer_id
        )
        filters = JobSeekerFilters(allow_notifications=True)
        jobseekers = self.jobseeker_service.get_all(filters=filters)
        self.notification_service.send_notification_group(
            message='New vacancy with skills that you have appeared!',
            objects=jobseekers,
        )
        return new_vacancy


@dataclass
class FilterCandidatesInVacancyUseCase:
    vacancy_service: BaseVacancyService

    def filter(
        self,
        interested_candidates: list[JobSeekerEntity],
        vacancy: VacancyEntity,
    ) -> list[JobSeekerEntity]:
        candidates: list[JobSeekerEntity] = []
        for candidate in interested_candidates:
            score = VacancyCriteria.get_candidate_rating(
                candidate=candidate, vacancy=vacancy
            )
            candidates.append((score, candidate))
        sorted_candidates_with_scores = self._sort_by_scores(candidates)
        sorted_candidates = list(
            map(lambda x: x[1], sorted_candidates_with_scores)
        )
        return sorted_candidates

    def _sort_by_scores(
        self, candidates: list[tuple[int, JobSeekerEntity]],
    ) -> list[tuple[int, JobSeekerEntity]]:
        sorted_candidates_with_scores = sorted(
            candidates,
            key=lambda x: x[0],
            reverse=True,
        )
        return sorted_candidates_with_scores

    def execute(
        self,
        vacancy_id: int,
        offset: int = 0,
        limit: int = 20,
    ) -> list[JobSeekerEntity]:
        vacancy: VacancyEntity = self.vacancy_service.get(id=vacancy_id)
        interested_candidates = self.vacancy_service.get_list_candidates(
            vacancy_id=vacancy_id,
            offset=offset,
            limit=limit,
        )
        candidates = self.filter(
            interested_candidates=interested_candidates,
            vacancy=vacancy,
        )
        return candidates
