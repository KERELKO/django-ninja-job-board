from abc import ABC, abstractmethod
from typing import Any


class BaseConverter(ABC):
    @abstractmethod
    def handle(self, obj: Any) -> Any: ...

    @abstractmethod
    def convert_to_entity(self, obj: Any) -> Any: ...
