from django.http import HttpRequest
from ninja import Query, Router

from src.common.filters.pagination import PaginationIn, PaginationOut

from src.apps.profiles.services.profiles import ORMJobSeekerProfileService
from src.apps.profiles.filters.profiles import ProfileFilters
from src.api.schemas import APIResponseSchema, ListPaginatedResponse

from .schemas import JobSeekerProfileOut


router = Router(tags=['jobseekers'])
service = ORMJobSeekerProfileService()


@router.get(
    '',
    response=APIResponseSchema[ListPaginatedResponse[JobSeekerProfileOut]]
)
def get_profile_list(
    request: HttpRequest,
    pagination_in: Query[PaginationIn],
    filters: Query[ProfileFilters],
) -> APIResponseSchema[ListPaginatedResponse[JobSeekerProfileOut]]:
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


@router.post('/{id}/apply/to/{vacancy_id}')
def apply_to_vacancy(
    request: HttpRequest,
    id: int,
    vacancy_id: int
) -> dict:
    service.apply_to_vacancy(profile_id=id, vacancy_id=vacancy_id)
    return {'Status': 'OK'}
