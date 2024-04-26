from dataclasses import dataclass
from typing import TypeVar

from django.core.mail import send_mail, send_mass_mail
from django.conf import settings

from celery import Task

from src.common.utils.celery import get_orm_models
from src.common.services.exceptions import NotificationException
from .base import BaseNotificationService


ET = TypeVar('ET')


@dataclass(unsafe_hash=True)
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


@dataclass(unsafe_hash=True)
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


@dataclass(unsafe_hash=True)
class ComposedNotificationService(BaseNotificationService):
    notification_services: tuple[BaseNotificationService]

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


@dataclass(unsafe_hash=True)
class CeleryNotificationService(BaseNotificationService, Task):
    notification_service: BaseNotificationService
    name: str = 'CeleryNotificationTaskService'

    def send_notification(
        self,
        message: str,
        subject: str,
        object: ET,
    ) -> None:
        self.delay(
            message=message,
            object_id=object.id,
            subject=subject,
            model_type=object.__class__.__name__,
        )

    def send_notification_group(
        self,
        message: str,
        objects: list[ET],
    ) -> None:
        first = next(objects)
        self.delay(
            message=message,
            object_ids=[first.id]+[o.id for o in objects],
            model_type=first.__class__.__name__,
            group=True,
        )

    def run(self, message: str, group: bool = False, **kwargs) -> None:
        if not group:
            object = get_orm_models(
                list_ids=[kwargs.get('object_id')],
                model_type=kwargs.get('model_type'),
                first=True,
            )
            self.notification_service.send_notification(
                object=object,
                message=message,
                subject=kwargs.get('subject', 'User'),
            )
        else:
            objects = get_orm_models(
                model_type=kwargs.get('model_type'),
                list_ids=kwargs.get('object_ids'),
            )
            self.notification_service.send_notification_group(
                message=message,
                objects=objects,
            )
