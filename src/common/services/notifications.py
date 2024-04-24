from dataclasses import dataclass
from typing import TypeVar
from django.core.mail import send_mail, send_mass_mail

from django.conf import settings

from .base import BaseNotificationService


ET = TypeVar('ET')


class EmailNotificationService(BaseNotificationService):
    def send_notification(
        self,
        message: str,
        object: ET,
        subject: str,
        from_email: str = settings.EMAIL_FROM,
    ) -> None:
        send_mail(
            message=message,
            subject=subject,
            from_email=from_email,
            recipient_list=[object.email],
            fail_silently=False,
        )

    def send_notification_group(
        self,
        message: str,
        objects: list[ET],
        from_email: str = settings.EMAIL_FROM,
    ) -> None:
        send_mass_mail(
            ((str(obj), message, from_email, [obj.email]) for obj in objects),
            fail_silently=False,
        )


class PhoneNotificationService(BaseNotificationService):
    def send_notification(
        self,
        message: str,
        subject: str,
        object: ET,
    ) -> None:
        print(f'{subject} with phone {object.phone} got a message:\n{message}')

    def send_notification_group(
        self,
        message: str,
        objects: list[ET],
    ) -> None:
        for obj in objects:
            print(f'{obj} with phone {obj.phone} got a message:\n{message}')


@dataclass
class ComposedNotificationService(BaseNotificationService):
    notification_services: list[BaseNotificationService]

    def send_notification(
        self,
        message: str,
        subject: str,
        object: ET,
    ) -> None:
        for service in self.notification_services:
            service.send_notification(message, subject, object)

    def send_notification_group(
        self,
        message: str,
        objects: list[ET],
    ) -> None:
        for service in self.notification_services:
            service.send_notification_group(message, objects)
