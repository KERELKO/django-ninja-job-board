from django.http import HttpRequest
from ninja import Router

from src.apps.vacancies.services import ORMVacancyService

from .schemas import VacancyOut


router = Router()
service = ORMVacancyService()


@router.get('/list', response=list[VacancyOut])
def get_vacancy_list(request: HttpRequest) -> list[VacancyOut]:
    vacancy_entity_list = service.get_vacancy_list()
    vacancy_list = [
        VacancyOut.from_entity(vacancy) for vacancy in vacancy_entity_list
    ]
    return vacancy_list
