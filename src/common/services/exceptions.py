from dataclasses import dataclass

from src.core.exceptions import ApplicationException


@dataclass
class ServiceException(ApplicationException):
    message: str

    def __str__(self) -> str:
        return self.message


@dataclass
class NotificationServiceException(ApplicationException):
    message: str

    def __str__(self) -> str:
        return self.message
