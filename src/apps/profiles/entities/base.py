from abc import abstractmethod
from dataclasses import dataclass


@dataclass
class BaseProfileEntity:
    id: int | None = None
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None

    @abstractmethod
    def to_dict(self) -> dict: ...
