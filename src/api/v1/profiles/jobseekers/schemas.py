from ninja import Schema

from src.apps.profiles.entities.profiles import (
    JobSeekerProfile as JobSeekerProfileEntity,
)


class BaseJobSeekerSchema(Schema):
    first_name: str
    last_name: str
    age: int
    about_me: str
    phone: str
    experience: int
    skills: list[str]


class JobSeekerProfileIn(BaseJobSeekerSchema):
    user_id: int


class JobSeekerProfileUpdate(BaseJobSeekerSchema):
    ...


class JobSeekerProfileOut(BaseJobSeekerSchema):
    id: int

    @staticmethod
    def from_entity(entity: JobSeekerProfileEntity) -> 'JobSeekerProfileOut':
        return JobSeekerProfileOut(**entity.to_dict())
