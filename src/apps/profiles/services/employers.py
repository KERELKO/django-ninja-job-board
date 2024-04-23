from typing import Iterable
from django.db.models import Q

from src.apps.profiles.entities.employers import EmployerEntity
from src.apps.profiles.models.employers import EmployerProfile
from src.apps.profiles.filters import EmployerFilter

from .base import BaseEmployerService


class ORMEmployerService(BaseEmployerService):
    def _build_queryset(self, filters: EmployerFilter) -> Q:
        query = Q()
        if filters.company_name:
            query &= Q(company_name=filters.company_name)
        return query

    def get_list(
        self,
        filters: EmployerFilter,
        offset: int,
        limit: int
    ) -> list[EmployerEntity]:
        query = self._build_queryset(filters)
        employers = EmployerProfile.objects.filter(query)[offset:offset+limit]
        return [self.converter.handle(employer) for employer in employers]

    def get_total_count(
        self,
        filters: EmployerFilter
    ) -> list[EmployerEntity]:
        query = self._build_queryset(filters)
        total_count = EmployerProfile.objects.filter(query).count()
        return total_count

    def get_all(self, filters: EmployerFilter) -> Iterable[EmployerEntity]:
        query = self._build_queryset(filters)
        for employer in EmployerProfile.objects.filter(query):
            yield employer

    def get(self, id: int) -> EmployerEntity:
        employer = EmployerProfile.objects.get(id=id)
        return self.converter.handle(employer)
