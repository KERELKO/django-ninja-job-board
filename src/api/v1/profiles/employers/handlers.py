from django.http import HttpRequest
from ninja import Query, Router

from src.apps.profiles.services.base import BaseEmployerProfileService
from src.apps.profiles.filters.profiles import EmployerFilter
from src.common.container import Container
from src.common.filters.pagination import PaginationIn, PaginationOut
from src.api.schemas import APIResponseSchema, ListPaginatedResponse
from src.api.v1.profiles.employers.schemas import EmployerProfileOut


router = Router(tags=['employers'])


@router.get(
    '',
    response=APIResponseSchema[ListPaginatedResponse[EmployerProfileOut]]
)
def get_employer_list(
    request: HttpRequest,
    filters: Query[EmployerFilter],
    pagination_in: Query[PaginationIn],
) -> APIResponseSchema[ListPaginatedResponse[EmployerProfileOut]]:
    service = Container.resolve(BaseEmployerProfileService)
    profile_list = service.get_list(
        filters=filters,
        offset=pagination_in.offset,
        limit=pagination_in.limit,
    )
    profile_count = service.get_total_count(filters=filters)
    pg_out = PaginationOut(
        offset=pagination_in.offset,
        limit=pagination_in.limit,
        total=profile_count,
    )
    data = ListPaginatedResponse(
        items=[EmployerProfileOut.from_entity(p) for p in profile_list],
        pagination=pg_out
    )
    return APIResponseSchema(data=data)
