from typing import Any
import pytest

from src.common.services.base import BaseNotificationService
from src.apps.profiles.services.base import BaseJobSeekerService
from src.apps.vacancies.services.base import BaseVacancyService
from src.apps.vacancies.use_cases.vacancies import (
    CreateVacancyUseCase,
    FilterCandidatesInVacancyUseCase,
)

from tests.services.conftest import (  # noqa
    vacancy_service,
    jobseeker_service,
    notification_service,
    logger,
)


@pytest.fixture
def vacancy_data() -> dict[str, Any]:
    data = {
        'title': 'Test',
        'description': 'Test vacancy description',
        'required_skills': ['python', 'docker'],
    }
    return data


@pytest.fixture
def create_vacancy_use_case(
    vacancy_service: BaseVacancyService,  # noqa
    jobseeker_service: BaseJobSeekerService,  # noqa
    notification_service: BaseNotificationService, # noqa
) -> CreateVacancyUseCase:
    return CreateVacancyUseCase(
        vacancy_service=vacancy_service,
        notification_service=notification_service,
        jobseeker_service=jobseeker_service,
    )


@pytest.fixture
def filter_candidates_in_vacancy_use_case(
    vacancy_service: BaseVacancyService  # noqa
) -> BaseVacancyService:
    return FilterCandidatesInVacancyUseCase(vacancy_service)
