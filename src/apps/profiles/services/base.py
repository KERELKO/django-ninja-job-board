from abc import abstractmethod

from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.common.services.base import BaseService


class BaseProfileService(BaseService): ...


class BaseJobSeekerService(BaseProfileService):
    @abstractmethod
    def update(self, id: int, **data) -> JobSeekerEntity: ...

    @abstractmethod
    def get_by_user_id(self, user_id: int) -> JobSeekerEntity: ...


class BaseEmployerService(BaseProfileService): ...
