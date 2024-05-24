from typing import Iterable

from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.apps.profiles.filters import JobSeekerFilters
from src.apps.profiles.services.base import BaseJobSeekerService


class FakeJobSeekerService(BaseJobSeekerService):
    def __init__(self, jobseeker: JobSeekerEntity) -> None:
        self.jobseekers = [jobseeker]

    def get_list(
        self, filters: JobSeekerFilters, offset: int = 0, limit: int = 20
    ) -> list[JobSeekerEntity]:
        return self.jobseekers[offset:limit]

    def get(self, id: int) -> JobSeekerEntity | None:
        for j in self.jobseekers:
            if j.id == id:
                return j
        return None

    def get_all(
        self,
        filters: JobSeekerFilters = JobSeekerFilters(allow_notifications=True),
    ) -> Iterable[JobSeekerEntity]:
        for j in self.jobseekers:
            yield j

    def get_total_count(self, filters: JobSeekerFilters) -> int:
        return len(self.jobseekers)

    def update(self, id: int, **data) -> JobSeekerEntity:
        ...

    def get_by_user_id(self, user_id: int) -> JobSeekerEntity:
        ...
