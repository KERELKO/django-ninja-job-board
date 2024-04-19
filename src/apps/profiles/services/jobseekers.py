from django.db.models import Q

from src.apps.vacancies.models.vacancies import Vacancy

from src.apps.profiles.entities.profiles import (
    JobSeekerProfile as JobSeekerProfileEntity,
)
from src.apps.profiles.models.profiles import JobSeekerProfile
from src.apps.profiles.filters.profiles import ProfileFilters

from .base import BaseJobSeekerProfileService


class ORMJobSeekerProfileService(BaseJobSeekerProfileService):

    def _build_queryset(self, filters: ProfileFilters) -> Q:
        query = Q()
        if filters.age__gte:
            query &= Q(age__gte=filters.age__gte)
        if filters.experience__gte:
            query &= Q(experience__gte=filters.experience__gte)
        if filters.skills:
            skills = [skill.lower() for skill in filters.skills]
            query &= Q(skills__contains=skills)
        return query

    def get_list(
        self,
        filters: ProfileFilters,
        offset: int = 0,
        limit: int = 20
    ) -> list[JobSeekerProfileEntity]:
        query = self._build_queryset(filters=filters)
        if filters.vacancy_id:
            vacancy = Vacancy.objects.prefetch_related(
                'interested_candidates'
                ).get(id=filters.vacancy_id)
            profile_list = vacancy.interested_candidates.filter(
                query
            )[offset:offset+limit]
        else:
            profile_list = JobSeekerProfile.objects.filter(
                query
            )[offset:offset+limit]
        return [self.converter.handle(profile) for profile in profile_list]

    def get_total_count(self, filters: ProfileFilters) -> int:
        query = self._build_queryset(filters)
        return JobSeekerProfile.objects.filter(query).count()

    def apply_to_vacancy(self, profile_id: int, vacancy_id: int) -> None:
        vacancy = Vacancy.objects.select_related(
            'employer'
        ).get(id=vacancy_id)
        vacancy.interested_candidates.add(profile_id)

        # Notifications, TODO: to move this code into another place
        subject = f'{vacancy.employer.first_name} {vacancy.employer.last_name}'
        self.notification_service.send_notification(
            subject=subject,
            message='Someone applied for your vacancy!',
            to=[vacancy.employer.email],
        )
