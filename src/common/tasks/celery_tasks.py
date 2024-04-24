from typing import TypeVar
from celery import shared_task

from src.common.services.notifications import (
    BaseNotificationService,
    EmailNotificationService,
    PhoneNotificationService,
)
from src.common.utils.celery import get_orm_models


T = TypeVar('T')
# Can't think up something better,
# Because Celery doesn't like classes and classes as parameters :(

# TODO: to solve this problem
# Cannot import notification service from Container due to circular imports
notification_service: BaseNotificationService = PhoneNotificationService()


@shared_task
def celery_notification_task(
    message: str,
    object_id: int,
    subject: str,
    model_type: str,
) -> None:
    object = get_orm_models(
        list_ids=[object_id],
        model_type=model_type,
        first=True,
    )
    notification_service.send_notification(
        object=object,
        message=message,
        subject=subject,
    )


@shared_task
def celery_notification_group_task(
    message: str,
    object_ids: list[int],
    model_type: str,
) -> None:
    objects = get_orm_models(model_type=model_type, list_ids=object_ids)
    notification_service.send_notification_group(
        message=message,
        objects=objects,
    )
