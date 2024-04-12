from django.http import HttpRequest
from ninja import Router, Query

from src.apps.vacancies.filters import VacancyFilters

from src.common.filters.pagination import PaginationIn, PaginationOut
from src.apps.vacancies.services import ORMVacancyService
from src.api.schemas import ListPaginatedResponse, APIResponseSchema

from .schemas import VacancyOut


router = Router()
service = ORMVacancyService()


@router.get(
    '/list',
    response=APIResponseSchema[ListPaginatedResponse[VacancyOut]]
)
def get_vacancy_list(
    request: HttpRequest,
    pagination_in: Query[PaginationIn],
    filters: Query[VacancyFilters]
) -> APIResponseSchema[ListPaginatedResponse[VacancyOut]]:
    vacancy_entity_list = service.get_vacancy_list(
        offset=pagination_in.offset,
        limit=pagination_in.limit,
        filters=filters,
    )
    vacancy_count = service.get_vacancy_count(filters=filters)
    vacancy_list = [
        VacancyOut.from_entity(vacancy) for vacancy in vacancy_entity_list
    ]
    pagination_out = PaginationOut(
        total=vacancy_count,
        offset=pagination_in.offset,
        limit=pagination_in.limit,
    )
    return APIResponseSchema(
        data=ListPaginatedResponse(
            items=vacancy_list,
            pagination=pagination_out,
        )
    )
