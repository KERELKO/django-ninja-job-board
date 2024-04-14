import pytest

from src.apps.vacancies.filters.vacancies import VacancyFilters

from .conftest import VacancyFactory


@pytest.mark.django_db
def test_get_empty_vacancy_list(vacancy_service):
    vacancies = vacancy_service.get_vacancy_list(VacancyFilters())
    assert len(vacancies) == 0


@pytest.mark.django_db
def test_get_vacancy_count_equals_to_zero(vacancy_service):
    vacancies_count = vacancy_service.get_vacancy_count(VacancyFilters())
    assert vacancies_count == 0


@pytest.mark.django_db
def test_get_vacancy_list(vacancy_service):
    VacancyFactory.create_batch(size=5)
    vacancies = vacancy_service.get_vacancy_list(VacancyFilters())
    assert len(vacancies) == 5
