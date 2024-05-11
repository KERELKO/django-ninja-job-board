import datetime
from logging import Logger
import random

import pytest
import factory

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


class JobSeekerEntityFactory(factory.Factory):
    class Meta:
        model = JobSeekerEntity

    id = random.randint(1, 300)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    age = random.randint(18, 32)
    phone = factory.Faker('phone_number')
    about_me = factory.Faker('sentence')
    experience = 2
    skills = ['python']
    allow_notifications = True


class VacancyEntityFactory(factory.Factory):
    class Meta:
        model = VacancyEntity

    title = factory.Faker('sentence')
    description = factory.Faker('text')
    created_at = datetime.datetime.now()


class EmployerEntityFactory(factory.Factory):
    class Meta:
        model = EmployerEntity

    id = random.randint(1, 300)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    company_name = 'Test company'


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
