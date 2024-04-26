from src.apps.profiles.filters import JobSeekerFilters
from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.apps.vacancies.entities import VacancyEntity

from .base import BaseVacancyUseCase


class CreateVacancyUseCase(BaseVacancyUseCase):
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


class FilterCandidatesInVacancyUseCase(BaseVacancyUseCase):
    def execute(self, vacancy_id: int) -> list[JobSeekerEntity]:
        ...
