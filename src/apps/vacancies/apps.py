from django.apps import AppConfig, apps


class VacanciesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.apps.vacancies"

    def ready(self):
        # TODO: to move this code into another place
        from src.common.services.base import BaseNotificationService
        from src.common.container import Container
        task = Container.resolve(BaseNotificationService)

        # Wait until all Django apps are ready
        if apps.apps_ready:
            from celery import current_app
            current_app.register_task(task)
