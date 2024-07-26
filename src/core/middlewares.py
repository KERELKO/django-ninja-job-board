from django.core.cache import cache
from django.http import HttpResponse, HttpRequest
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


class ApiCacheMiddleware(MiddlewareMixin):
    def process_request(self, request) -> HttpResponse | None:
        # Check if the request is for an API endpoint
        if request.path.startswith('/api/'):
            cache_key = self._get_cache_key(request)
            cached_response = cache.get(cache_key)
            if cached_response:
                return HttpResponse(cached_response)

    def process_response(self, request: HttpRequest, response: HttpResponse) -> HttpResponse:
        # Cache the response for API requests
        if request.path.startswith('/api/') and response.status_code == 200:
            cache_key = self._get_cache_key(request)
            cache.set(
                cache_key, response.content, timeout=settings.DEFAULT_RESPONSE_CACHE_TIMEOUT
            )
        return response

    def _get_cache_key(self, request: HttpRequest) -> str:
        return f'api_cache_{request.get_full_path()}'
