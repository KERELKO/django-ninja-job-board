from functools import lru_cache
from logging import Logger, getLogger

import punq

from src.common.services.base import (
    BaseNotificationService,
)
from src.common.services.notifications import (
    CeleryNotificationService,
    ComposedNotificationService,
    EmailNotificationService,
    PhoneNotificationService,
)
from src.apps.profiles.services.employers import ORMEmployerService
from src.apps.profiles.services.jobseekers import ORMJobSeekerService
from src.apps.vacancies.use_cases.vacancies import (
    CreateVacancyUseCase,
    FilterCandidatesInVacancyUseCase,
)
from src.apps.profiles.use_cases.jobseekers import (
    ApplyToVacancyUseCase,
    UpdateJobSeekerProfileUseCase,
)
from src.apps.profiles.services.base import (
    BaseEmployerService,
    BaseJobSeekerService,
)
from src.apps.vacancies.services.vacancies import (
    BaseVacancyService,
    ORMVacancyService,
)
from src.apps.vacancies.converters import ORMVacancyConverter

class Container:
    @lru_cache(1)
    @staticmethod
    def get():
        return Container._init()

    @staticmethod
    def resolve(cls):
        return Container.get().resolve(cls)

    @staticmethod
    def _init():
        container = punq.Container()

        # Logger
        lg = getLogger("custom")
        container.register(Logger, instance=lg)

        # Notification Service
        celery_notification_service = CeleryNotificationService(
            notification_service=ComposedNotificationService(
                notification_services=(
                    EmailNotificationService(lg),
                    PhoneNotificationService(lg),
                )
            ),
            logger=lg,
        )
        container.register(
            BaseNotificationService,
            instance=celery_notification_service,
        )

        # JobSeeker Profile Service
        orm_jobseeker_service = ORMJobSeekerService(logger=lg)
        container.register(
            BaseJobSeekerService,
            instance=orm_jobseeker_service,
        )

        # Employer Profile Service
        orm_employer_service = ORMEmployerService(logger=lg)
        container.register(
            BaseEmployerService,
            instance=orm_employer_service,
        )

        # Vacancy Service
        orm_vacancy_service = ORMVacancyService(
            converter=ORMVacancyConverter(),
            jobseeker_service=orm_jobseeker_service,
            employer_service=orm_employer_service,
            logger=lg,
        )
        container.register(
            BaseVacancyService,
            instance=orm_vacancy_service,
        )

        # Use Cases
        container.register(CreateVacancyUseCase)
        container.register(ApplyToVacancyUseCase)
        container.register(FilterCandidatesInVacancyUseCase)
        container.register(UpdateJobSeekerProfileUseCase)

        return container
