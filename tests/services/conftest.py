from factory.django import DjangoModelFactory
import pytest

from src.apps.vacancies.models.vacancies import Vacancy
from src.apps.profiles.models.profiles import JobSeekerProfile, EmployerProfile
from src.apps.vacancies.services.vacancies import ORMVacancyService


class JobSeekerProfileFactory(DjangoModelFactory):
    required_skills = ['first_name']

    class Meta:
        model = JobSeekerProfile


class EmployerProfileFactory(DjangoModelFactory):
    class Meta:
        model = EmployerProfile


class VacancyFactory(DjangoModelFactory):
    slug = 'slug'
    required_skills = ['first_name']
    employer = EmployerProfileFactory.create_batch(size=1)
    interested_candidates = JobSeekerProfileFactory.create_batch(size=3)

    class Meta:
        model = Vacancy


@pytest.fixture
def vacancy_service():
    return ORMVacancyService()
