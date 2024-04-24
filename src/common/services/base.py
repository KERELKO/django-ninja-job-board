from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable, TypeVar, Any


ET = TypeVar('ET')


class BaseService(ABC):
    @abstractmethod
    def get_list(self, filters: Any, offset: int, limit: int) -> list[ET]:
        ...

    @abstractmethod
    def get_total_count(self, filters: Any) -> int:
        ...

    @abstractmethod
    def get(self, id: int) -> ET:
        ...

    @abstractmethod
    def get_all(self, filters: Any) -> Iterable[ET]:
        ...


class BaseNotificationService(ABC):
    @abstractmethod
    def send_notification(
        self,
        message: str,
        subject: str,
        object: ET,
    ) -> None:
        ...

    @abstractmethod
    def send_notification_group(
        self,
        message: str,
        objects: list[ET]
    ) -> None:
        ...


@dataclass
class BaseBackgroundTaskService:
    notification_service: BaseNotificationService

    @abstractmethod
    def send_notification_task(
        self,
        message: str,
        subject: str,
        object: ET,
    ) -> None:
        self.notification_service.send_notification_task(
            message=message,
            subject=subject,
            object=object,
        )

    @abstractmethod
    def send_notification_group_task(
        self,
        message: str,
        objects: Iterable[ET],
    ) -> None:
        self.notification_service.send_notification_group_task(
            message=message,
            objects=objects,
        )
