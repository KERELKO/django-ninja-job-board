from django.http import HttpRequest
from ninja import Router


router = Router(tags=['employers'])


@router.get('', response=dict)
def get_profiles(request: HttpRequest) -> dict:
    return {'ping': 'pong'}
