from dataclasses import dataclass, field
from typing import Callable
from celery import shared_task

from .notifications import EmailNotificationService


# Can't think up something better,
# Because Celery doesn't like classes :(


@shared_task
def celery_email_notification(**kwargs):
    EmailNotificationService().send_notification(**kwargs)


@dataclass
class CeleryTaskObserver:
    notification_tasks: list[Callable] = field(default_factory=list)

    def send_notification_task(self, **kwargs):
        for task in self.notification_tasks:
            task.delay(**kwargs)
