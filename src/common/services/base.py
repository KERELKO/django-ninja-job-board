from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable, TypeVar, Any


# Entity TypeVar
ET = TypeVar('ET')


@dataclass
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


@dataclass
class BaseNotificationService(ABC):
    @abstractmethod
    def send_notification(
        self,
        message: str,
        subject: str,
        to: ET,
    ) -> None:
        ...

    @abstractmethod
    def send_notification_group(
        self,
        message: str,
        objects: list[ET]
    ) -> None:
        ...


class BaseBackgroundTaskService:
    @abstractmethod
    def send_notification_task(
        self,
        message: str,
        subject: str,
        to: ET,
    ) -> None:
        ...

    @abstractmethod
    def send_notification_task_group(
        self,
        message: str,
        objects: Iterable[ET],
    ) -> None:
        ...
