from dataclasses import dataclass

from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.apps.vacancies.entities import VacancyEntity
from src.apps.profiles.services.base import BaseJobSeekerService
from src.apps.vacancies.services.base import BaseVacancyService
from src.common.services.base import BaseNotificationService


@dataclass
class ApplyToVacancyUseCase:
    vacancy_service: BaseVacancyService
    notification_service: BaseNotificationService

    def execute(self, candidate_id: int, vacancy_id: int) -> None:
        vacancy: VacancyEntity = self.vacancy_service.get(id=vacancy_id)
        self.vacancy_service.add_candidate(
            candidate_id=candidate_id,
            vacancy_id=vacancy_id,
        )

        employer = vacancy.employer
        self.notification_service.send_notification(
            object=employer,
            message=(
                f'Someone applied for your vacancy with title: {vacancy.title}'
            ),
            subject=f'{employer.first_name} {employer.last_name}',
        )


@dataclass
class UpdateJobSeekerProfileUseCase:
    jobseeker_service: BaseJobSeekerService

    def execute(self, profile: JobSeekerEntity) -> JobSeekerEntity:
        updated_profile = self.jobseeker_service.update(entity=profile)
        return updated_profile
