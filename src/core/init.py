from logging import Logger

from django.apps import AppConfig
from django.conf import settings


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

        # Init Celery worker
        service = Container.resolve(BaseNotificationService)
        if service.__class__ == CeleryNotificationService:
            logger.info(
                'Using Celery worker',
                extra={'info': f'__class__: {service.__class__}'}
            )
            current_app.register_task(service)  # type: ignore
        else:
            logger.warning(
                msg='BaseNotificationService is not Celery task',
                extra={'info': f'__class__: {service.__class__}'},
            )
        # Log information about cache
        cache_backend = settings.CACHES['default']['BACKEND']
        cache_location = settings.CACHES['default']['LOCATION']
        logger.info(
            f'Cache backend: {cache_backend}',
            extra={'info': f'location: {cache_location}'},
        )
