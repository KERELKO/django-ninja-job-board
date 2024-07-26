from django.http import Http404, HttpRequest
from ninja import Query, Router
from ninja.security import django_auth

from src.api.schemas import APIResponseSchema, ListPaginatedResponse
from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.apps.profiles.filters import JobSeekerFilters
from src.apps.profiles.services.base import BaseJobSeekerService
from src.apps.profiles.use_cases.jobseekers import (
    ApplyToVacancyUseCase, UpdateJobSeekerProfileUseCase,
)
from src.common.container import Container
from src.common.filters.pagination import PaginationIn, PaginationOut
from src.common.services.exceptions import ServiceException

from .schemas import JobSeekerProfileOut, JobSeekerProfileUpdate

router = Router(tags=['jobseekers'])


@router.get(
    '', response=APIResponseSchema[ListPaginatedResponse[JobSeekerProfileOut]]
)
def get_profile_list(
    request: HttpRequest,
    pagination_in: Query[PaginationIn],
    filters: Query[JobSeekerFilters],
) -> APIResponseSchema[ListPaginatedResponse[JobSeekerProfileOut]]:
    service = Container.resolve(BaseJobSeekerService)
    profile_entities = service.get_list(
        filters=filters,
        offset=pagination_in.offset,
        limit=pagination_in.limit,
    )
    total_profile_count = service.get_total_count(filters=filters)
    schemas = [
        JobSeekerProfileOut.from_entity(entity) for entity in profile_entities
    ]
    profiles_list = ListPaginatedResponse(
        items=schemas,
        pagination=PaginationOut(
            offset=pagination_in.offset,
            limit=pagination_in.limit,
            total=total_profile_count,
        ),
    )
    response = APIResponseSchema(data=profiles_list)
    return response


@router.post(
    '/{id}/apply/to/{vacancy_id}',
    response=APIResponseSchema[dict[str, str]],
    description="""
        This handler takes jobseeker profile id as first parameter
        and vacancy_id as the second,
        adds the profile to the list of interested candidates for the vacancy,
        and sends notification to the employer
    """,
)
def apply_to_vacancy(
    request: HttpRequest, id: int, vacancy_id: int
) -> APIResponseSchema[dict[str, str]]:
    use_case = Container.resolve(ApplyToVacancyUseCase)
    try:
        use_case.execute(candidate_id=id, vacancy_id=vacancy_id)
    except ServiceException as e:
        raise Http404(e)
    return APIResponseSchema(data={'Status': 'OK'})


@router.get(
    '/me',
    response=APIResponseSchema[JobSeekerProfileOut],
    auth=django_auth,
)
def get_my_profile(
    request: HttpRequest,
) -> APIResponseSchema[JobSeekerProfileOut]:
    service = Container.resolve(BaseJobSeekerService)
    try:
        profile = service.get_by_user_id(user_id=request.user.id)  # type: ignore
    except ServiceException as e:
        raise Http404(e)
    response = APIResponseSchema(data=JobSeekerProfileOut.from_entity(profile))
    return response


@router.patch('/{id}', response=APIResponseSchema[JobSeekerProfileOut])
def update_profile(
    request: HttpRequest,
    id: int,
    profile: Query[JobSeekerProfileUpdate],
) -> APIResponseSchema[JobSeekerProfileOut]:
    use_case = Container.resolve(UpdateJobSeekerProfileUseCase)
    entity = JobSeekerEntity(id=id, **profile.model_dump())
    try:
        updated_profile = use_case.execute(profile=entity)
    except ServiceException as e:
        raise Http404(e)
    return APIResponseSchema(
        data=JobSeekerProfileOut.from_entity(updated_profile)
    )
