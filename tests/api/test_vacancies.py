import httpx


def test_can_get_vacancy_list():
    response = httpx.get('http://localhost:8000/api/vacancies')
    assert response.status_code == 200


def test_can_get_vacancy_list_with_filters():
    response = httpx.get(
        'http://localhost:8000/api/vacancies?'
        'offset=0&limit=10&search=test&is_remote=true'
        '&required_experience__gte=1&required_skills=test&'
        'location=test&company_name=test&salary__gte=1000&salary__lte=0'
    )
    assert response.status_code == 200


def test_can_create_vacancy(dummy_vacancy):
    response = httpx.post(
        'http://localhost:8000/api/vacancies',
        json=dummy_vacancy,
    )
    assert response.status_code == 200
