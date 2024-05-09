from logging import Logger
from django.apps import AppConfig


class InitConfig(AppConfig):
    """
    Initialize config
    """

    name = 'src.core.init'

    def ready(self):
        from celery import current_app

        from src.common.services.base import BaseNotificationService
        from src.common.services.notifications import CeleryNotificationService
        from src.common.container import Container

        logger = Container.resolve(Logger)

        service = Container.resolve(BaseNotificationService)
        if service.__class__ == CeleryNotificationService:
            current_app.register_task(service)
        else:
            logger.warning(
                msg='BaseNotificationService is not Celery task',
                extra={'info': f'__class__: {service.__class__}'},
            )
