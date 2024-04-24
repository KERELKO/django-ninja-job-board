from dataclasses import dataclass


class ApplicationException(Exception):
    ...


@dataclass
class ServiceException(ApplicationException):
    message: str

    def __str__(self) -> str:
        return self.message


@dataclass
class NotificationException(ApplicationException):
    message: str

    def __str__(self) -> str:
        return self.message
