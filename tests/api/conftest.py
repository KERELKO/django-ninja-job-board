from typing import Any

import pytest


@pytest.fixture
def dummy_vacancy() -> dict[str, Any]:
    data = {
        'title': 'Test vacancy',
        'description': 'test',
        'company_name': 'Test',
        'created_at': '2024-05-11T08:59:31.552Z',
        'salary': 2000,
        'required_skills': [
          'python', 'django', 'fastapi', 'docker',
        ],
        'is_remote': True,
        'location': 'string',
        'required_experience': 0,
        'employer_id': 1
    }
    return data
