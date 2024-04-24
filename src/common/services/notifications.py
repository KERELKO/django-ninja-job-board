from dataclasses import dataclass
from typing import TypeVar
from django.core.mail import send_mail, send_mass_mail

from django.conf import settings

from src.common.services.exceptions import NotificationException

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
        try:
            email = object.email
        except AttributeError:
            raise NotificationException(f'{subject} does not have an email')
        send_mail(
            message=message,
            subject=subject,
            from_email=from_email,
            recipient_list=[email],
            fail_silently=False,
        )

    def send_notification_group(
        self,
        message: str,
        objects: list[ET],
        from_email: str = settings.EMAIL_FROM,
    ) -> None:
        data = []
        for obj in objects:
            try:
                email = obj.email
            except AttributeError:
                continue
                # TODO: to log the exception
            data.append((str(obj), message, from_email, (email,)))
        send_mass_mail(
            data,
            fail_silently=False,
        )


class PhoneNotificationService(BaseNotificationService):
    def send_notification(
        self,
        message: str,
        subject: str,
        object: ET,
    ) -> None:
        try:
            phone = object.phone
        except AttributeError:
            raise NotificationException(
                f'{subject} does not have a phone number'
            )
        print(f'{subject} with phone {phone} got a message:\n{message}')

    def send_notification_group(
        self,
        message: str,
        objects: list[ET],
    ) -> None:
        for obj in objects:
            try:
                phone = object.phone
            except AttributeError:
                continue
            print(f'{obj} with phone {phone} got a message:\n{message}')


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
