from typing import Iterable, TypeVar

from src.apps.profiles.entities.employers import EmployerEntity
from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.apps.profiles.models.employers import EmployerProfile
from src.apps.profiles.models.jobseekers import JobSeekerProfile


T = TypeVar('T')


def get_orm_models(
    model_type: str,
    objects_ids: list[int],
    first: bool = False,
) -> Iterable[T] | T:
    '''
    Returns a list of Django orm models or a single object if first=True
    '''
    if model_type in [JobSeekerProfile.__name__, JobSeekerEntity.__name__]:
        objects = JobSeekerProfile.objects.filter(id__in=objects_ids)
    elif model_type in [EmployerProfile.__name__, EmployerEntity.__name__]:
        objects = EmployerProfile.objects.filter(id__in=objects_ids)
    else:
        raise ValueError('Invalid model type', model_type)
    if first:
        return objects.first()
    return objects.all()
