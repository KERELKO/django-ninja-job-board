from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.apps.vacancies.use_cases.vacancies import (
    FilterCandidatesInVacancyUseCase
)
from src.apps.vacancies.entities import VacancyEntity
from src.apps.vacancies.enums import VacancyCriteria
from tests.use_cases.conftest import CreateVacancyUseCase


def test_create_use_case_can_be_executed_without_errors(
    create_vacancy_use_case: CreateVacancyUseCase,
    vacancy: VacancyEntity,
) -> None:
    new_vacancy = create_vacancy_use_case.execute(
        employer_id=1, entity=vacancy
    )
    assert isinstance(new_vacancy, VacancyEntity)


def test_filter_candidates_in_use_case_execute(
    filter_candidates_in_vacancy_use_case: FilterCandidatesInVacancyUseCase,
) -> None:
    vacancy = filter_candidates_in_vacancy_use_case.vacancy_service.get(id=1)
    assert vacancy is not None
    candidates = filter_candidates_in_vacancy_use_case.execute(vacancy_id=1)
    assert isinstance(candidates, list)
    if len(candidates) > 0:
        c = candidates[0]
        assert isinstance(c, JobSeekerEntity)
        for skill in c.skills:
            if skill in vacancy.required_skills:
                assert True
                break


def test_filter_candidates_in_vacancy_use_case(
    filter_candidates_in_vacancy_use_case: FilterCandidatesInVacancyUseCase,
) -> None:
    vacancy: VacancyEntity = filter_candidates_in_vacancy_use_case.vacancy_service.get(id=1)  # noqa
    if not vacancy:
        assert False, 'No vacancy with id: 1'
    if len(vacancy.interested_candidates) < 5:
        assert False, 'not enough candidates to test the function'
    # usecase result
    usecase_result = filter_candidates_in_vacancy_use_case.execute(
        vacancy_id=1
    )
    # VacancyCriteria result
    vacancy_criteria_result = []
    for c in vacancy.interested_candidates:
        rating = VacancyCriteria.get_candidate_rating(
            candidate=c, vacancy=vacancy
        )
        vacancy_criteria_result.append((rating, c))
    sorted_candidates = sorted(
        vacancy_criteria_result,
        key=lambda x: x[0],
        reverse=True,
    )
    for i in range(len(vacancy.interested_candidates)):
        if sorted_candidates[i][1] != usecase_result[i]:
            assert False
