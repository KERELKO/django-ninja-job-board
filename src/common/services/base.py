from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, Any


T = TypeVar('T')


@dataclass
class BaseService(ABC):
    @abstractmethod
    def get_list(self, filters: Any, offset: int, limit: int) -> list[T]:
        ...

    @abstractmethod
    def get_total_count(self, filters) -> int:
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


class BaseBackgroundTaskService:
    ...
