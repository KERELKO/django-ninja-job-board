from dataclasses import dataclass

from src.core.exceptions import ApplicationException


@dataclass
class IncorrectModelTypeError(ApplicationException, TypeError):
    model_type: str

    def __str__(self) -> str:
        return f'Incorrect passed model_type argument: {self.model_type}'
