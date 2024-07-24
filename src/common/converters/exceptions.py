from dataclasses import dataclass
from typing import Any


class ConverterException(Exception):
    ...


@dataclass
class IncorrectConverterArgument(ConverterException):
    obj: Any
    choices: list[Any]
    _message: str | None = None

    @property
    def message(self):
        if self._message:
            return self._message
        elif self.choices:
            return (
                f'Incorrect passed converter argument, argument: {self.obj}\n'
                + f'Choices are: {self.choices}'
            )
        else:
            return (
                f'Incorrect passed converter argument, argument: {self.obj}\n'
            )
