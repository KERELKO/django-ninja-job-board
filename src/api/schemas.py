from typing import TypeVar, Generic

from ninja import Field, Schema as Schema

from core.common.filters.pagination import PaginationOut


TData = TypeVar('TData')
TListItem = TypeVar('TListItem')


class ListPaginatedRespoonse(Schema, Generic[TListItem]):
    items: TListItem = Field(default_factory=list)
    pagination: PaginationOut


class APIResponseSchema(Schema, Generic[TData]):
    data: TData | dict = Field(default_factory=dict)
    meta: dict = Field(default_factory=dict)
    errors: dict = Field(default_factory=dict)
