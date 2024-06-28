from abc import ABC, abstractmethod
from typing import Iterable, TypeVar, Any, Generic


ET = TypeVar('ET')


class BaseService(Generic[ET], ABC):
    @abstractmethod
    def get_list(self, filters: Any, offset: int, limit: int) -> list[ET]: ...

    @abstractmethod
    def get_total_count(self, filters: Any) -> int: ...

    @abstractmethod
    def get(self, id: int) -> ET | None: ...

    @abstractmethod
    def get_all(self, filters: Any) -> Iterable[ET]: ...


class BaseNotificationService(Generic[ET], ABC):
    @abstractmethod
    def send_notification(
        self,
        message: str,
        subject: str,
        object: ET,
    ) -> None: ...

    @abstractmethod
    def send_notification_group(
        self, message: str, objects: Iterable[ET]
    ) -> None: ...
