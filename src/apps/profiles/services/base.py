from dataclasses import dataclass

from src.common.converters.base import BaseConverter
from src.common.services.base import BaseService


@dataclass
class BaseProfileService(BaseService):
    converter: BaseConverter


@dataclass
class BaseJobSeekerService(BaseProfileService):
    ...


@dataclass
class BaseEmployerService(BaseProfileService):
    ...
