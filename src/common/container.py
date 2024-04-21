import punq

from src.common.services.tasks import CeleryTaskObserver, celery_email_notification
from src.apps.profiles.converters.employers import ORMEmployerProfileConverter
from src.apps.profiles.services.employers import ORMEmployerProfileService
from src.apps.profiles.services.jobseekers import ORMJobSeekerProfileService
from src.apps.profiles.converters.jobseekers import (
    ORMJobSeekerProfileConverter,
)
from src.apps.profiles.services.base import (
    BaseEmployerProfileService,
    BaseJobSeekerProfileService,
)
from src.apps.vacancies.services.vacancies import (
    BaseVacancyService,
    ORMVacancyService,
)
from src.apps.vacancies.converters.vacancies import ORMVacancyConverter

from src.common.services.base import BaseBackgroundTaskService, BaseNotificationService
from src.common.services.notifications import EmailNotificationService


class Container:

    @staticmethod
    def get():
        return Container._init()

    @staticmethod
    def resolve(cls):
        return Container._init().resolve(cls)

    @staticmethod
    def _init():
        container = punq.Container()

        # Background Task Service
        container.register(
            BaseBackgroundTaskService,
            CeleryTaskObserver,
            notification_tasks=[
                celery_email_notification,
            ]
        )

        # Notifiction Service
        container.register(
            BaseNotificationService,
            EmailNotificationService
        )

        # JobSeeker Profile Service
        container.register(
            BaseJobSeekerProfileService,
            ORMJobSeekerProfileService,
            converter=ORMJobSeekerProfileConverter(),
        )

        # Employer Profile Service
        container.register(
            BaseEmployerProfileService,
            ORMEmployerProfileService,
            converter=ORMEmployerProfileConverter(),
        )

        # Vacancy Service
        container.register(
            BaseVacancyService,
            ORMVacancyService,
            converter=ORMVacancyConverter()
        )

        return container
