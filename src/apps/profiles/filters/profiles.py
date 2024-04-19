from pydantic import BaseModel, Field


class ProfileFilters(BaseModel):
    skills: list[str] = Field(default_factory=list)
    age__gte: int = 18
    experience__gte: int = 0
    vacancy_id: int = 0


class EmployerFilter(BaseModel):
    ...
