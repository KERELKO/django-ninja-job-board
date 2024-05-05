from dataclasses import dataclass

from src.apps.profiles.filters import JobSeekerFilters
from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.apps.profiles.services.base import (
    BaseEmployerService,
    BaseJobSeekerService,
)
from src.apps.vacancies.entities import VacancyEntity
from src.apps.vacancies.services.base import BaseVacancyService
from src.common.services.base import BaseNotificationService


@dataclass
class CreateVacancyUseCase:
    vacancy_service: BaseVacancyService
    jobseeker_service: BaseJobSeekerService
    notification_service: BaseNotificationService

    def execute(self, employer_id: int, **vacancy_data) -> VacancyEntity:
        new_vacancy = self.vacancy_service.create(
            employer_id=employer_id,
            **vacancy_data,
        )
        filters = JobSeekerFilters(
            allow_notifications=True,
        )
        jobseekers = self.jobseeker_service.get_all(filters=filters)
        self.notification_service.send_notification_group(
            message='New vacancy with skills that you have appeared!',
            objects=jobseekers,
        )
        return new_vacancy


@dataclass
class FilterCandidatesInVacancyUseCase:
    vacancy_service: BaseVacancyService
    employer_service: BaseEmployerService
    jobseeker_service: BaseJobSeekerService
    notification_service: BaseNotificationService

    def execute(
        self,
        vacancy_id: int,
        offset: int,
        limit: int,
    ) -> list[JobSeekerEntity]:
        candidates = self.vacancy_service.filter_candidates(
            vacancy_id=vacancy_id,
            offset=offset,
            limit=limit,
        )
        return candidates
