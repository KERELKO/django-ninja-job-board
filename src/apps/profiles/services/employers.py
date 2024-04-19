from django.db.models import Q

from src.apps.profiles.entities.profiles import (
    EmployerProfile as EmployerProfileEntity,
)
from src.apps.profiles.models.profiles import EmployerProfile
from .base import BaseEmployerProfileService


class ORMEmployerProfileService(BaseEmployerProfileService):
    def _build_queryset(filters):
        query = Q()
        return query

    def get_list(
        self,
        filters,
        offset: int,
        limit: int
    ) -> list[EmployerProfileEntity]:
        query = self._build_queryset(filters)
        employers = EmployerProfile.objects.filter(query)[offset:offset+limit]
        return [self.converter.handle(employer) for employer in employers]

    def get_total_count(self, filters) -> list[EmployerProfileEntity]:
        query = self._build_queryset(filters)
        total_count = EmployerProfile.objects.filter(query).count()
        return total_count
