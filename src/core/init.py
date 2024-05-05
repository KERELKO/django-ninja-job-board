from django.apps import AppConfig


class InitConfig(AppConfig):
    """
    Initialize config
    """

    name = 'src.core.init'

    def ready(self):
        from src.common.services.base import BaseNotificationService
        from src.common.services.notifications import CeleryNotificationService
        from src.common.container import Container
        from celery import current_app

        service = Container.resolve(BaseNotificationService)
        if service.__class__ == CeleryNotificationService:
            current_app.register_task(service)
