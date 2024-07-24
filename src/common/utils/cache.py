from typing import Any, Callable

from django.conf import settings
from django.core.cache import cache
from django.http import HttpRequest


def generate_cache_key_from_request(request: HttpRequest) -> str:
    """Construct cache key based on request URL path and query parameters"""
    list_params = []
    for param, val in request.GET.items():
        list_params.append(f'{param}={val}')
    return f'{request.path}' + ''.join(list_params)


# TODO: to make somehow this class work
class cache_handler:  # noqa
    def __init__(
        self,
        timeout: int = settings.DEFAULT_RESPONSE_CACHE_TIMEOUT
    ) -> None:
        self.timeout = timeout

    def __call__(self, func: Callable) -> Callable:
        def wrapper(request: HttpRequest, *args, **kwargs) -> Any | dict:
            cache_key = generate_cache_key_from_request(request)
            response = cache.get(cache_key)
            if response:
                return response
            handler_response = func(request, *args, **kwargs)
            cache.set(cache_key, self.timeout)
            return handler_response
        return wrapper
