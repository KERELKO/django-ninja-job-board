from abc import abstractmethod
from dataclasses import dataclass

from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.common.converters.base import BaseConverter
from src.common.services.base import BaseService


@dataclass
class BaseProfileService(BaseService):
    converter: BaseConverter


@dataclass
class BaseJobSeekerService(BaseProfileService):
    @abstractmethod
    def update(self, id: int, **data) -> JobSeekerEntity:
        ...

    @abstractmethod
    def get_by_user_id(self, user_id: int) -> JobSeekerEntity:
        ...


@dataclass
class BaseEmployerService(BaseProfileService):
    ...
