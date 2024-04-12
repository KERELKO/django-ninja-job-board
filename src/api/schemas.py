from typing import Any, TypeVar, Generic

from ninja import Field, Schema

from src.common.filters.pagination import PaginationOut


TData = TypeVar('TData')
TListItem = TypeVar('TListItem')


class ListPaginatedResponse(Schema, Generic[TListItem]):
    items: list[TListItem] = Field(default_factory=list)
    pagination: PaginationOut


class APIResponseSchema(Schema, Generic[TData]):
    data: TData | dict = Field(default_factory=dict)
    meta: dict = Field(default_factory=dict)
    errors: list[Any] = Field(default_factory=list)
