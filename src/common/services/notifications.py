from dataclasses import dataclass
from typing import Iterable, TypeVar
from logging import Logger

from django.core.mail import send_mail, send_mass_mail
from django.conf import settings

from celery import Task

from src.core.exceptions import ApplicationException
from src.common.models.exeptions import IncorrectModelTypeError
from src.common.utils.orm import get_orm_models
from src.common.services.exceptions import NotificationServiceException

from .base import BaseNotificationService


ET = TypeVar('ET')


@dataclass(unsafe_hash=True)
class EmailNotificationService(BaseNotificationService[ET]):
    logger: Logger

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
            self.logger.warning(
                msg=f'"{subject}" does not have an email address',
                extra={'info': f'cls: {object.__class__}, id: {object.id}'},
            )
            raise NotificationServiceException(
                f'{subject} does not have an email'
            )
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
        objects: Iterable[ET],
        from_email: str = settings.EMAIL_FROM,
    ) -> None:
        data = []
        for obj in objects:
            try:
                email = obj.email
            except AttributeError:
                self.logger.warning(
                    msg=f'"{obj}" does not have an email address',
                    extra={'info': f'cls: {obj.__class__}, id: {obj.id}'},
                )
                continue
            data.append((str(obj), message, from_email, (email,)))
        send_mass_mail(
            data,
            fail_silently=False,
        )


@dataclass(unsafe_hash=True)
class PhoneNotificationService(BaseNotificationService[ET]):
    logger: Logger

    def send_notification(
        self,
        message: str,
        subject: str,
        object: ET,
    ) -> None:
        try:
            phone = object.phone
        except AttributeError:
            self.logger.warning(
                msg=f'"{subject}" does not have an phone number',
                extra={'info': f'cls: {object.__class__}, id: {object.id}'},
            )
            raise NotificationServiceException(
                f'{subject} does not have a phone number'
            )
        print(f'{subject} with phone {phone} got a message:\n{message}')

    def send_notification_group(
        self,
        message: str,
        objects: Iterable[ET],
    ) -> None:
        for obj in objects:
            try:
                phone = obj.phone
            except AttributeError:
                self.logger.warning(
                    msg=f'"{obj}" does not have a phone number',
                    extra={'info': f'cls: {obj.__class__}, id: {obj.id}'},
                )
                continue
            print(f'{obj} with phone {phone} got a message:\n{message}')


@dataclass(unsafe_hash=True)
class ComposedNotificationService(BaseNotificationService[ET]):
    notification_services: tuple[BaseNotificationService]

    def send_notification(
        self,
        message: str,
        subject: str,
        object: ET,
    ) -> None:
        for service in self.notification_services:
            service.send_notification(
                message=message,
                subject=subject,
                object=object,
            )

    def send_notification_group(
        self,
        message: str,
        objects: Iterable[ET],
    ) -> None:
        for service in self.notification_services:
            service.send_notification_group(
                message=message,
                objects=objects,
            )


@dataclass(unsafe_hash=True)
class CeleryNotificationService(BaseNotificationService[ET], Task):
    logger: Logger
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
        objects: Iterable[ET],
    ) -> None:
        try:
            first_object = next(objects)
        except StopIteration:
            self.logger.info(
                msg='"Objects" argument is empty',
                extra={'info': f'{objects}'},
            )
            return
        self.delay(
            message=message,
            object_ids=[first_object.id] + [o.id for o in objects],
            model_type=first_object.__class__.__name__,
            group=True,
        )

    def run(self, message: str, group: bool = False, **kwargs) -> None:
        if not group:
            try:
                object = get_orm_models(
                    list_ids=[kwargs.get('object_id')],
                    model_type=kwargs.get('model_type'),
                    first=True,
                )
            except IncorrectModelTypeError as e:
                self.logger.error(
                    msg=f'Invalid model type {e.model_type}',
                )
                raise ApplicationException(e)
            self.notification_service.send_notification(
                object=object,
                message=message,
                subject=kwargs.get('subject', 'User'),
            )
        else:
            try:
                objects = get_orm_models(
                    model_type=kwargs.get('model_type'),
                    list_ids=kwargs.get('object_ids'),
                )
            except IncorrectModelTypeError as e:
                self.logger.error(
                    msg=f'Invalid model type {e.model_type}',
                )
                raise ApplicationException(e)
            self.notification_service.send_notification_group(
                message=message,
                objects=objects,
            )
