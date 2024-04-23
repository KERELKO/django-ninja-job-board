from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable, TypeVar, Any


# Entity TypeVar
TE = TypeVar('TE')


@dataclass
class BaseService(ABC):
    @abstractmethod
    def get_list(self, filters: Any, offset: int, limit: int) -> list[TE]:
        ...

    @abstractmethod
    def get_total_count(self, filters: Any) -> int:
        ...

    @abstractmethod
    def get(self, id: int) -> TE:
        ...

    @abstractmethod
    def get_all(self, filters: Any) -> Iterable[TE]:
        ...


@dataclass
class BaseNotificationService(ABC):
    @abstractmethod
    def send_notification(
        self,
        message: str,
        subject: str,
        to: list[str],
    ) -> None:
        ...

    @abstractmethod
    def send_notification_group(
        self,
        message: str,
        recipient_list: list[tuple[str, str]],
    ) -> None:
        ...


class BaseBackgroundTaskService:
    ...
