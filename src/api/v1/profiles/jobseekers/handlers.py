from django.http import HttpRequest
from ninja import Query, Router

from src.common.container import Container
from src.common.filters.pagination import PaginationIn, PaginationOut
from src.apps.profiles.services.base import BaseJobSeekerProfileService
from src.apps.profiles.filters.profiles import ProfileFilters
from src.api.schemas import APIResponseSchema, ListPaginatedResponse

from .schemas import JobSeekerProfileOut


router = Router(tags=['jobseekers'])


@router.get(
    '',
    response=APIResponseSchema[ListPaginatedResponse[JobSeekerProfileOut]]
)
def get_profile_list(
    request: HttpRequest,
    pagination_in: Query[PaginationIn],
    filters: Query[ProfileFilters],
) -> APIResponseSchema[ListPaginatedResponse[JobSeekerProfileOut]]:
    service = Container.resolve(BaseJobSeekerProfileService)
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
            total=total_profile_count
        )
    )
    return APIResponseSchema(data=profiles_list)


@router.post(
    '/{id}/apply/to/{vacancy_id}',
    response=APIResponseSchema[dict[str, str]],
    description='''
        This handler takes jobseeker profile id as first parameter
        and vacancy_id as the second,
        adds the profile to the list of interested candidates for the vacancy,
        and sends notification to the employer
    '''
)
def apply_to_vacancy(
    request: HttpRequest,
    id: int,
    vacancy_id: int
) -> APIResponseSchema[dict[str, str]]:
    service = Container.resolve(BaseJobSeekerProfileService)
    service.apply_to_vacancy(profile_id=id, vacancy_id=vacancy_id)
    return APIResponseSchema(data={'Status': 'OK'})


# TODO: to make this handler work
@router.get('/my', response=APIResponseSchema[JobSeekerProfileOut])
def get_my_profile(
    request: HttpRequest,
) -> APIResponseSchema[JobSeekerProfileOut]:
    ...
