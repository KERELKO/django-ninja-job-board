from django.conf import settings
from django.http import Http404, HttpRequest
from django.core.cache import cache
from ninja import Router, Query
from src.common.utils.cache import generate_cache_key_from_request
from src.api.v1.profiles.jobseekers.schemas import JobSeekerProfileOut
from src.apps.profiles.filters import JobSeekerFilters
from src.apps.profiles.services.base import BaseJobSeekerService
from src.common.services.exceptions import ServiceException
from src.apps.vacancies.use_cases.vacancies import (
    CreateVacancyUseCase,
    FilterCandidatesInVacancyUseCase,
)
from src.common.container import Container
from src.apps.vacancies.filters import VacancyFilters
from src.apps.vacancies.services.vacancies import BaseVacancyService

from src.common.filters.pagination import PaginationIn, PaginationOut
from src.api.schemas import ListPaginatedResponse, APIResponseSchema

from .schemas import VacancyIn, VacancyOut


router = Router(tags=['vacancies'])


@router.get('', response=APIResponseSchema[ListPaginatedResponse[VacancyOut]])
def get_vacancy_list(
    request: HttpRequest,
    pagination_in: Query[PaginationIn],
    filters: Query[VacancyFilters],
) -> APIResponseSchema[ListPaginatedResponse[VacancyOut]]:
    cache_key = generate_cache_key_from_request(request)
    response = cache.get(cache_key)
    if response:
        return response
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
    response = APIResponseSchema(
        data=ListPaginatedResponse(
            items=vacancy_list,
            pagination=pagination_out,
        )
    )
    cache.set(
        cache_key,
        response.model_dump(),
        timeout=settings.DEFAULT_RESPONSE_CACHE_TIMEOUT,
    )
    return response


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
    return APIResponseSchema(data=VacancyOut.from_entity(vacancy_entity))


@router.get(
    '/{id}/filter',
    response=APIResponseSchema[ListPaginatedResponse[JobSeekerProfileOut]],
)
def filter_candidates_in_vacancy(
    request: HttpRequest,
    pagination_in: Query[PaginationIn],
    vacancy_id: int,
) -> APIResponseSchema[ListPaginatedResponse[JobSeekerProfileOut]]:
    cache_key = generate_cache_key_from_request(request)
    print(cache_key)
    response = cache.get(cache_key)
    if response:
        return response
    response = cache.get(cache_key)
    if response:
        return response
    usecase = Container.resolve(FilterCandidatesInVacancyUseCase)
    jobseeker_service = Container.resolve(BaseJobSeekerService)
    total = jobseeker_service.get_total_count(
        filters=JobSeekerFilters(vacancy_id=vacancy_id)
    )
    candidates = usecase.execute(
        vacancy_id=vacancy_id,
        offset=pagination_in.offset,
        limit=pagination_in.limit,
    )
    data = ListPaginatedResponse(
        items=candidates,
        pagination=PaginationOut(
            total=total,
            offset=pagination_in.offset,
            limit=pagination_in.limit,
        ),
    )
    response = APIResponseSchema(data=data)
    cache.set(cache_key, response.model_dump())
    return response
