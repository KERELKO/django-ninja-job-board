from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.apps.vacancies.entities import VacancyEntity
from src.apps.vacancies.filters import VacancyFilters
from src.apps.vacancies.services.base import BaseVacancyService


def test_can_get_vacancy_list(vacancy_service: BaseVacancyService):
    vacancies = vacancy_service.get_list(filters=VacancyFilters())
    assert isinstance(vacancies, list)


def test_can_get_vacancy_count(vacancy_service: BaseVacancyService):
    vacancy_count = vacancy_service.get_total_count(filters=VacancyFilters())
    assert isinstance(vacancy_count, int)


def test_can_get_vacancy_by_id(vacancy_service: BaseVacancyService):
    vacancy = vacancy_service.get(id=1)
    assert vacancy is not None
    assert isinstance(vacancy, VacancyEntity)


def test_can_get_candidates_in_vacancy(vacancy_service: BaseVacancyService):
    vacancy = vacancy_service.get(id=1)
    if not vacancy:
        assert False, 'No vacancy with id "1"'
    candidates = vacancy_service.get_list_candidates(vacancy_id=1)
    assert isinstance(candidates, list)
    if len(candidates) > 0:
        assert isinstance(candidates[0], JobSeekerEntity)


def test_can_add_interested_candidate_in_vacancy(
    vacancy_service: BaseVacancyService
):
    vacancy = vacancy_service.get(id=1)
    if not vacancy:
        assert False, 'No vacancy with id "1"'
    lcandidates = len(vacancy.interested_candidates)
    vacancy_service.add_candidate(candidate_id=1, vacancy_id=1)
    assert lcandidates + 1 == len(vacancy.interested_candidates)
