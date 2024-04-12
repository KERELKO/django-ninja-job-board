from ninja import Schema as ResponseSchema
from pydantic import BaseModel


class BaseSchema(BaseModel):
    ...


class BaseResponseSchema(ResponseSchema):
    ...
