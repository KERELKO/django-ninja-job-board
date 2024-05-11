import datetime
from logging import Logger
import random

import pytest
import factory

from tests.fake.services.vacancies import FakeVacancyService
from src.apps.vacancies.services.base import BaseVacancyService
from src.common.services.notifications import (
    ComposedNotificationService,
    PhoneNotificationService,
    EmailNotificationService,
)
from src.common.services.base import BaseNotificationService
from src.apps.profiles.entities.employers import EmployerEntity
from src.apps.vacancies.entities import VacancyEntity
from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.common.container import Container


available_skills = [
    'python', 'django', 'fastapi', 'docker', 'redis', 'sql', 'postgresql',
    'rabbitmq', 'design patterns', 'algorithms', 'pytest', 'javascript',
    'css', 'html', 'mongodb', 'tests', 'architecture', 'oop', 'devops',
    'vue.js', 'angular', 'rust', 'c++', 'flask', 'sqlalchemy', 'asyncio',
]


class EmployerEntityFactory(factory.Factory):
    class Meta:
        model = EmployerEntity

    id = random.randint(1, 20)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    company_name = 'Test company'


class JobSeekerEntityFactory(factory.Factory):
    class Meta:
        model = JobSeekerEntity

    id = random.randint(1, 20)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    age = random.randint(18, 32)
    phone = factory.Faker('phone_number')
    about_me = factory.Faker('sentence')
    experience = 2
    skills = random.choices(available_skills, k=8)
    allow_notifications = True


class VacancyEntityFactory(factory.Factory):
    class Meta:
        model = VacancyEntity

    title = factory.Faker('sentence')
    employer = EmployerEntityFactory.build()
    description = factory.Faker('text')
    created_at = datetime.datetime.now()
    interested_candidates = JobSeekerEntityFactory.create_batch(6)
    required_skills = random.choices(available_skills, k=2)


@pytest.fixture
def logger() -> Logger:
    return Container.resolve(Logger)


@pytest.fixture
def notification_service(logger) -> BaseNotificationService:
    services = [
        EmailNotificationService,
        PhoneNotificationService,
        ComposedNotificationService,
    ]
    service = random.choice(services)
    if service == services[-1]:
        service = ComposedNotificationService((
                EmailNotificationService(logger),
                PhoneNotificationService(logger)
            ),
        )
        return service
    else:
        return service(logger)


@pytest.fixture
def jobseeker_entity() -> JobSeekerEntity:
    return JobSeekerEntityFactory.build()


@pytest.fixture
def jobseeker_entity_group() -> list[JobSeekerEntity]:
    jobseekers = JobSeekerEntityFactory.build_batch(5)
    return jobseekers


@pytest.fixture
def vacancy_entity() -> VacancyEntity:
    return VacancyEntityFactory.build()


@pytest.fixture
def employer_entity() -> EmployerEntity:
    return EmployerEntityFactory.build()


@pytest.fixture
def vacancy_service() -> BaseVacancyService:
    vacancy_entity = VacancyEntityFactory.build(id=1)
    return FakeVacancyService(vacancy_entity)
