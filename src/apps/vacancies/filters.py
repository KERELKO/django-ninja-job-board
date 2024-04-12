from pydantic import BaseModel


class VacancyFilters(BaseModel):
    search: str | None = None
