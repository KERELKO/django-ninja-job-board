from ninja import Schema
from pydantic import ConfigDict

from src.apps.profiles.entities.employers import EmployerEntity


class BaseEmployerProfileSchema(Schema):
    first_name: str
    last_name: str
    email: str
    company_name: str = ''


class EmployerProfileOut(BaseEmployerProfileSchema):
    id: int

    @staticmethod
    def from_entity(entity: EmployerEntity) -> 'EmployerProfileOut':
        return EmployerProfileOut(**entity.to_dict())


class EmployerProfileIn(BaseEmployerProfileSchema):
    user_id: int


class EmployerProfileUpdate(BaseEmployerProfileSchema):
    model_config = ConfigDict(extra='forbid')
