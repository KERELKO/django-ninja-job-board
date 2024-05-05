from django.db.models import QuerySet

from typing import TypeVar

from src.common.models.exeptions import IncorrectModelTypeError

from src.apps.profiles.entities.employers import EmployerEntity
from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.apps.profiles.models.employers import EmployerProfile
from src.apps.profiles.models.jobseekers import JobSeekerProfile
from src.apps.vacancies.entities import VacancyEntity
from src.apps.vacancies.models import Vacancy


T = TypeVar('T')


def get_orm_models(
    model_type: str,
    list_ids: list[int],
    first: bool = False,
) -> QuerySet[T] | T:
    '''
    Returns a list of Django models or a single object if first=True
    '''
    if model_type in [JobSeekerProfile.__name__, JobSeekerEntity.__name__]:
        objects = JobSeekerProfile.objects.filter(id__in=list_ids)
    elif model_type in [EmployerProfile.__name__, EmployerEntity.__name__]:
        objects = EmployerProfile.objects.filter(id__in=list_ids)
    elif model_type in [VacancyEntity.__name__, Vacancy.__name__]:
        objects = Vacancy.objects.filter(id__in=list_ids)
    else:
        raise IncorrectModelTypeError(model_type)
    if first:
        return objects.first()
    return objects.all()
