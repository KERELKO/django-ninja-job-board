import pytest

from src.common.services.exceptions import NotificationServiceException
from src.common.services.base import BaseNotificationService


def test_notification_service_can_send_notifications(
    notification_service: BaseNotificationService, jobseeker_entity
) -> None:
    try:
        notification_service.send_notification(
            message='Hello',
            object=jobseeker_entity,
            subject='Test',
        )
    except Exception:
        assert False


def test_notification_service_can_send_notifications_group(
    notification_service: BaseNotificationService, jobseeker_entity_group,
) -> None:
    try:
        notification_service.send_notification_group(
            message='Hi all!',
            objects=jobseeker_entity_group,
        )
    except Exception:
        assert False


def test_notification_service_can_not_send_notifications(
    notification_service: BaseNotificationService, vacancy_entity
) -> None:
    with pytest.raises(NotificationServiceException):
        notification_service.send_notification(
            message='Hi vacancy!',
            object=vacancy_entity,
            subject='Test',
        )
