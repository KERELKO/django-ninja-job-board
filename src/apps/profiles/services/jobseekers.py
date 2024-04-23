from typing import Iterable
from django.db.models import Q

from src.apps.vacancies.models import Vacancy

from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.apps.profiles.models.jobseekers import JobSeekerProfile
from src.apps.profiles.filters import JobSeekerFilters

from .base import BaseJobSeekerService


# TODO: to handle Exceptions
class ORMJobSeekerService(BaseJobSeekerService):

    def _build_queryset(self, filters: JobSeekerFilters) -> Q:
        query = Q()
        if filters.age__gte:
            query &= Q(age__gte=filters.age__gte)
        if filters.experience__gte:
            query &= Q(experience__gte=filters.experience__gte)
        if filters.skills:
            skills = [skill.lower() for skill in filters.skills]
            query &= Q(skills__contains=skills)
        if filters.allow_notifications:
            query &= Q(allow_notifications=filters.allow_notifications)
        return query

    def get_list(
        self,
        filters: JobSeekerFilters,
        offset: int = 0,
        limit: int = 20
    ) -> list[JobSeekerEntity]:
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

    def get(self, id: int) -> JobSeekerEntity:
        profile = JobSeekerProfile.objects.get(id=id)
        return self.converter.handle(profile)

    def get_all(self, filters: JobSeekerFilters) -> Iterable[JobSeekerEntity]:
        query = self._build_queryset(filters=filters)
        for jobseeker in JobSeekerProfile.objects.filter(query):
            yield jobseeker

    def get_total_count(self, filters: JobSeekerFilters) -> int:
        query = self._build_queryset(filters)
        return JobSeekerProfile.objects.filter(query).count()

    def update(self, id: int, **data) -> JobSeekerEntity:
        profile = JobSeekerProfile.objects.get(id=id)
        for field, value in data.items():
            if value is not None:
                if hasattr(profile, field):
                    setattr(profile, field, value)
        profile.save()
        return self.converter.handle(profile)

    def get_by_user_id(self, user_id: int) -> JobSeekerEntity:
        profile = JobSeekerProfile.objects.filter(user_id=user_id).first()
        return self.converter.handle(profile)
