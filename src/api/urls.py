from django.urls import path
from ninja import NinjaAPI

from .v1.vacancies.handlers import router as vacancy_router
from .v1.profiles.employers.handlers import router as employer_profiler_router
from .v1.profiles.jobseekers.handlers import (
    router as jobseeker_profiler_router,
)


api = NinjaAPI()

api.add_router(prefix='/v1/vacancies', router=vacancy_router)
api.add_router(prefix='/v1/jobseekers', router=jobseeker_profiler_router)
api.add_router(prefix='/v1/employers', router=employer_profiler_router)
urlpatterns = [
    path('', api.urls),
]
