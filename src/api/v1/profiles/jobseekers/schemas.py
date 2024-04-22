from ninja import Schema

from src.apps.profiles.entities.jobseekers import JobSeekerEntity


class BaseJobSeekerProfileSchema(Schema):
    first_name: str
    last_name: str
    age: int
    about_me: str
    phone: str
    experience: int
    skills: list[str]


class JobSeekerProfileIn(BaseJobSeekerProfileSchema):
    user_id: int


class JobSeekerProfileUpdate(BaseJobSeekerProfileSchema):
    ...


class JobSeekerProfileOut(BaseJobSeekerProfileSchema):
    id: int

    @staticmethod
    def from_entity(entity: JobSeekerEntity) -> 'JobSeekerProfileOut':
        return JobSeekerProfileOut(**entity.to_dict())
