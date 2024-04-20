from dataclasses import dataclass

from src.common.converters.base import BaseConverter
from src.common.services.base import (
    BaseBackgroundTaskService,
    BaseNotificationService,
    BaseService,
)


@dataclass
class BaseProfileService(BaseService):
    converter: BaseConverter


@dataclass
class BaseJobSeekerProfileService(BaseProfileService):
    notification_service: BaseNotificationService
    task_service: BaseBackgroundTaskService


@dataclass
class BaseEmployerProfileService(BaseProfileService):
    ...
