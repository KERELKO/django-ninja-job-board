from src.apps.profiles.entities.jobseekers import JobSeekerEntity

from .base import BaseProfileUseCase


class ApplyToVacancyUseCase(BaseProfileUseCase):
    def execute(self, candidate_id: int, vacancy_id: int) -> None:
        vacancy = self.vacancy_service.get(id=vacancy_id)
        self.vacancy_service.add_candidate(
            candidate_id=candidate_id,
            vacancy_id=vacancy_id,
        )

        employer = vacancy.employer
        self.notification_service.send_notification(
            object=employer,
            message=(
                'Someone applied for your vacancy'
                f'with title: {vacancy.title}'
            ),
            subject=f'{employer.first_name} {employer.last_name}'
        )


class UpdateJobSeekerProfileUseCase(BaseProfileUseCase):
    def execute(
        self,
        profile_id: int,
        **data,
    ) -> JobSeekerEntity:
        updated_profile = self.jobseeker_service.update(
            id=profile_id,
            **data,
        )
        return updated_profile
