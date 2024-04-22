from dataclasses import dataclass

from src.apps.profiles.services.base import (
    BaseEmployerService,
    BaseJobSeekerService,
)
from src.apps.vacancies.services.base import BaseVacancyService
from src.common.services.base import BaseBackgroundTaskService
from src.common.use_cases.base import BaseUseCase


@dataclass
class BaseVacancyUseCase(BaseUseCase):
    vacancy_service: BaseVacancyService
    employer_service: BaseEmployerService
    jobseeker_service: BaseJobSeekerService
    task_service: BaseBackgroundTaskService
