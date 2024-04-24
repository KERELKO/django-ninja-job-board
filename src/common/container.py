import punq

from src.apps.vacancies.use_cases.vacancies import (
    CreateVacancyUseCase,
    FilterCandidatesInVacancyUseCase,
)
from src.apps.profiles.use_cases.jobseekers import (
    ApplyToVacancyUseCase,
    UpdateJobSeekerProfileUseCase,
)
from src.common.services.tasks import CeleryTaskService
from src.apps.profiles.converters.employers import ORMEmployerConverter
from src.apps.profiles.services.employers import ORMEmployerService
from src.apps.profiles.services.jobseekers import ORMJobSeekerService
from src.apps.profiles.converters.jobseekers import (
    ORMJobSeekerConverter,
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

from src.common.services.base import (
    BaseBackgroundTaskService,
    BaseNotificationService,
)
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
            CeleryTaskService,
        )

        # Notifiction Service
        container.register(
            BaseNotificationService,
            EmailNotificationService
        )

        # JobSeeker Profile Service
        container.register(
            BaseJobSeekerService,
            ORMJobSeekerService,
            converter=ORMJobSeekerConverter(),
        )

        # Employer Profile Service
        container.register(
            BaseEmployerService,
            ORMEmployerService,
            converter=ORMEmployerConverter(),
        )

        # Vacancy Service
        container.register(
            BaseVacancyService,
            ORMVacancyService,
            converter=ORMVacancyConverter()
        )

        # Use Cases
        container.register(CreateVacancyUseCase)
        container.register(ApplyToVacancyUseCase)
        container.register(FilterCandidatesInVacancyUseCase)
        container.register(UpdateJobSeekerProfileUseCase)

        return container
