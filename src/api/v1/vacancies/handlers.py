from django.http import Http404, HttpRequest
from ninja import Router, Query

from src.common.services.exceptions import ServiceException
from src.apps.vacancies.use_cases.vacancies import CreateVacancyUseCase
from src.common.container import Container
from src.apps.vacancies.filters import VacancyFilters
from src.apps.vacancies.services.vacancies import BaseVacancyService

from src.common.filters.pagination import PaginationIn, PaginationOut
from src.api.schemas import ListPaginatedResponse, APIResponseSchema

from .schemas import VacancyIn, VacancyOut


router = Router(tags=['vacancies'])


# TODO: tests
@router.get('', response=APIResponseSchema[ListPaginatedResponse[VacancyOut]])
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
    usecase = Container.resolve(CreateVacancyUseCase)
    data = vacancy_data.model_dump()
    employer_id = data.pop('employer_id')
    try:
        vacancy_entity = usecase.execute(
            employer_id=employer_id,
            **data,
        )
    except ServiceException as e:
        raise Http404(e)
    return APIResponseSchema(data=VacancyOut(**vacancy_entity.to_dict()))
