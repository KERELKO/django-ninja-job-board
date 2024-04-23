from src.apps.profiles.filters import JobSeekerFilters
from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.apps.vacancies.entities import VacancyEntity

from .base import BaseVacancyUseCase


# TODO: add mass notification about publish of the vacancy
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
        for jobseeker in jobseekers:
            print(jobseeker)
            self.task_service.send_notification_task(
                message='New vacancy with skills that you have appeared!',
                subject=f'{jobseeker.first_name} {jobseeker.last_name}',
                to=[jobseeker.email],
            )
        return new_vacancy


class FilterCandidatesInVacancyUseCase(BaseVacancyUseCase):
    def execute(self, vacancy_id: int) -> list[JobSeekerEntity]:
        ...
