from django.http import HttpRequest
from ninja import Router, Query

from src.common.container import Container
from src.apps.vacancies.filters.vacancies import VacancyFilters
from src.apps.vacancies.services.vacancies import BaseVacancyService

from src.common.filters.pagination import PaginationIn, PaginationOut
from src.api.schemas import ListPaginatedResponse, APIResponseSchema

from .schemas import VacancyIn, VacancyOut, VacancyUpdate


router = Router(tags=['vacancies'])


# TODO: tests
@router.get(
    '',
    response=APIResponseSchema[ListPaginatedResponse[VacancyOut]]
)
def get_vacancy_list(
    request: HttpRequest,
    pagination_in: Query[PaginationIn],
    filters: Query[VacancyFilters],
) -> APIResponseSchema[ListPaginatedResponse[VacancyOut]]:
    service = Container.resolve(BaseVacancyService)
    vacancy_entity_list = service.get_list(
        offset=pagination_in.offset,
        limit=pagination_in.limit,
        filters=filters,
    )
    vacancy_count = service.get_total_count(filters=filters)
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


@router.post('', response=APIResponseSchema[VacancyOut])
def create_vacancy(
    request: HttpRequest,
    vacancy_data: VacancyIn,
) -> APIResponseSchema[VacancyOut]:
    service = Container.resolve(BaseVacancyService)
    vacancy_entity = service.create(**vacancy_data.model_dump())
    return APIResponseSchema(data=VacancyOut(**vacancy_entity.to_dict()))


@router.get('/{id}', response=APIResponseSchema[VacancyOut])
def get_vacancy(
    request: HttpRequest,
    id: int
) -> APIResponseSchema[VacancyOut]:
    service = Container.resolve(BaseVacancyService)
    vacancy_entity = service.get(id)
    return APIResponseSchema(data=VacancyOut.from_entity(vacancy_entity))


@router.patch('/{id}', response=APIResponseSchema[VacancyOut])
def update_vacancy(
    request: HttpRequest,
    id: int,
    vacancy_data: VacancyUpdate,
) -> APIResponseSchema[VacancyOut]:
    service = Container.resolve(BaseVacancyService)
    updated_vacancy = service.update(id, **vacancy_data.model_dump())
    return APIResponseSchema(data=updated_vacancy)


@router.delete('/{id}', response=APIResponseSchema[dict[str, str]])
def delete_vacancy(
    request: HttpRequest,
    vacancy_id: int,
) -> APIResponseSchema[dict[str, str]]:
    service = Container.resolve(BaseVacancyService)
    service.delete(id=vacancy_id)
    return APIResponseSchema(data={'Status': 'OK'})
