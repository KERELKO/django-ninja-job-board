from abc import abstractmethod
from dataclasses import dataclass


@dataclass
class BaseProfileEntity:
    id: int
    first_name: str
    last_name: str
    email: str

    @abstractmethod
    def to_dict(self) -> dict: ...
