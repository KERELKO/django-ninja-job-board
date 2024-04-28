from django.apps import AppConfig, apps


class InitConfig(AppConfig):
    '''
    Initialize config
    '''

    name = 'src.core.init'

    def ready(self):
        from src.common.services.base import BaseNotificationService
        from src.common.container import Container
        task = Container.resolve(BaseNotificationService)

        # Wait until all Django apps are ready
        if apps.apps_ready:
            from celery import current_app
            current_app.register_task(task)
