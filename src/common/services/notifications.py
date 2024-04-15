from django.core.mail import send_mail

from django.conf import settings

from .base import BaseNotificationService


class EmailNotificationService(BaseNotificationService):
    def send_notification(
        self,
        message: str,
        to: list[str],
        subject: str,
        from_email: str = settings.EMAIL_FROM,
    ) -> None:
        send_mail(
            message=message,
            subject=subject,
            from_email=from_email,
            recipient_list=to,
            fail_silently=False,
        )
