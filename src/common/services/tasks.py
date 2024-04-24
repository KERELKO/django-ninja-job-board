from dataclasses import dataclass
from typing import Callable, Iterable, TypeVar

from src.common.tasks.celery_tasks import (
    celery_notification_group_task,
    celery_notification_task,
)

from .base import BaseBackgroundTaskService


T = TypeVar('T')


@dataclass
class CeleryTaskService(BaseBackgroundTaskService):
    celery_notification_task: Callable = celery_notification_task
    celery_notification_group_task: Callable = celery_notification_group_task

    def send_notification_task(
        self,
        message: str,
        subject: str,
        object: T,
    ) -> None:
        print(object.__class__.__name__)
        self.celery_notification_task.delay(
            message=message,
            object_id=object.id,
            subject=subject,
            model_type=object.__class__.__name__,
        )

    def send_notification_group_task(
        self,
        message: str,
        objects: Iterable[T],
    ) -> None:
        first = next(objects)
        self.celery_notification_group_task.delay(
            message=message,
            objects_ids=[first.id]+[o.id for o in objects],
            model_type=first.__class__.__name__,
        )
