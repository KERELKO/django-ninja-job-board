from django.db.models import Q

from src.apps.profiles.entities.profiles import (
    EmployerProfile as EmployerProfileEntity,
)
from src.apps.profiles.models.profiles import EmployerProfile
from src.apps.profiles.filters.profiles import EmployerFilter

from .base import BaseEmployerProfileService


class ORMEmployerProfileService(BaseEmployerProfileService):
    def _build_queryset(self, filters: EmployerFilter):
        query = Q()
        if filters.company_name:
            query &= Q(company_name=filters.company_name)
        return query

    def get_list(
        self,
        filters: EmployerFilter,
        offset: int,
        limit: int
    ) -> list[EmployerProfileEntity]:
        query = self._build_queryset(filters)
        employers = EmployerProfile.objects.filter(query)[offset:offset+limit]
        return [employer.to_entity() for employer in employers]

    def get_total_count(
        self,
        filters: EmployerFilter
    ) -> list[EmployerProfileEntity]:
        query = self._build_queryset(filters)
        total_count = EmployerProfile.objects.filter(query).count()
        return total_count
