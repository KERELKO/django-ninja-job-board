from ninja import Schema
from pydantic import ConfigDict

from src.apps.profiles.entities.employers import EmployerEntity


class EmployerProfileOut(Schema):
    id: int
    first_name: str
    last_name: str
    email: str
    company_name: str = ''

    @classmethod
    def from_entity(cls, entity: EmployerEntity) -> 'EmployerProfileOut':
        return cls(**entity.to_dict())


class EmployerProfileIn(Schema):
    user_id: int
    first_name: str
    last_name: str
    email: str
    company_name: str = ''


class EmployerProfileUpdate(Schema):
    model_config = ConfigDict(extra='forbid')
    first_name: str
    last_name: str
    email: str
    company_name: str = ''
