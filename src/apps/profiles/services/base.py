from dataclasses import dataclass
from src.common.converters.base import BaseConverter
from src.common.services.base import BaseNotificationService, BaseService


@dataclass
class BaseProfileService(BaseService):
    converter: BaseConverter


@dataclass
class BaseJobSeekerProfileService(BaseProfileService):
    notification_service: BaseNotificationService


@dataclass
class BaseEmployerProfileService(BaseProfileService):
    ...
