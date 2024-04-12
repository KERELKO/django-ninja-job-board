from pydantic import BaseModel


class PaginationIn(BaseModel):
    offset: int = 0
    limit: int = 20


class PaginationOut(BaseModel):
    offset: int
    limit: int
    total: int
