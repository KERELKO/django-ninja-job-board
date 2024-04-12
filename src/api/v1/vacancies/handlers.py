from django.http import HttpRequest
from ninja import Router, Query

from src.apps.vacancies.filters import VacancyFilters

from src.core.common.filters.pagination import PaginationIn
from src.apps.vacancies.services import ORMVacancyService

from .schemas import VacancyOut


router = Router()
service = ORMVacancyService()


@router.get('/list', response=list[VacancyOut])
def get_vacancy_list(
    request: HttpRequest,
    pagination_in: Query[PaginationIn],
    filters: Query[VacancyFilters]
) -> list[VacancyOut]:
    vacancy_entity_list = service.get_vacancy_list(
        offset=pagination_in.offset,
        limit=pagination_in.limit,
        filters=filters,
    )
    vacancy_list = [
        VacancyOut.from_entity(vacancy) for vacancy in vacancy_entity_list
    ]
    return vacancy_list
