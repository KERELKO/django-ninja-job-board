from django.urls import path
from ninja import NinjaAPI

from .v1.vacancies.handlers import router as vacancy_router


api = NinjaAPI()
api.add_router(prefix='/vacancies', router=vacancy_router)


urlpatterns = [
    path('v1/', api.urls),
]
