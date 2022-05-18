"""
MIT License

Copyright (c) 2022-present japandotorg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from _typeshed import Self
from collections.abc import Iterator
from typing import Any, Generic, TypeVar

from ..sql.annotation import SupportsCloneAnnotations
from ..sql.base import Executable
from ..sql.selectable import (
    GroupedElement,
    HasHints,
    HasPrefixes,
    HasSuffixes,
    SelectBase,
    _SelectFromElements,
)
from . import interfaces
from .context import QueryContext as QueryContext
from .util import aliased as aliased

__all__ = ["Query", "QueryContext", "aliased"]

_T = TypeVar("_T")

class Query(
    _SelectFromElements,
    SupportsCloneAnnotations,
    HasPrefixes,
    HasSuffixes,
    HasHints,
    Executable,
    Generic[_T],
):
    logger: Any
    load_options: Any
    session: Any
    def __init__(self, entities, session: Any | None = ...) -> None: ...
    @property
    def statement(self): ...
    def subquery(
        self, name: str | None = ..., with_labels: bool = ..., reduce_columns: bool = ...
    ): ...
    def cte(self, name: Any | None = ..., recursive: bool = ..., nesting: bool = ...): ...
    def label(self, name): ...
    def as_scalar(self): ...
    def scalar_subquery(self): ...
    @property
    def selectable(self): ...
    def __clause_element__(self): ...
    def only_return_tuples(self: Self, value) -> Self: ...
    @property
    def is_single_entity(self): ...
    def enable_eagerloads(self: Self, value) -> Self: ...
    def with_labels(self): ...
    apply_labels: Any
    @property
    def get_label_style(self): ...
    def set_label_style(self, style): ...
    def enable_assertions(self: Self, value) -> Self: ...
    @property
    def whereclause(self): ...
    def with_polymorphic(
        self: Self, cls_or_mappers, selectable: Any | None = ..., polymorphic_on: Any | None = ...
    ) -> Self: ...
    def yield_per(self: Self, count) -> Self: ...
    def get(self, ident): ...
    @property
    def lazy_loaded_from(self): ...
    def correlate(self: Self, *fromclauses) -> Self: ...
    def autoflush(self: Self, setting) -> Self: ...
    def populate_existing(self: Self) -> Self: ...
    def with_parent(self, instance, property: Any | None = ..., from_entity: Any | None = ...): ...
    def add_entity(self: Self, entity, alias: Any | None = ...) -> Self: ...
    def with_session(self: Self, session) -> Self: ...
    def from_self(self, *entities): ...
    def values(self, *columns): ...
    def value(self, column): ...
    def with_entities(self: Self, *entities) -> Self: ...
    def add_columns(self: Self, *column) -> Self: ...
    def add_column(self, column): ...
    def options(self: Self, *args) -> Self: ...
    def with_transformation(self, fn): ...
    def get_execution_options(self): ...
    def execution_options(self: Self, **kwargs) -> Self: ...
    def with_for_update(
        self: Self,
        read: bool = ...,
        nowait: bool = ...,
        of: Any | None = ...,
        skip_locked: bool = ...,
        key_share: bool = ...,
    ) -> Self: ...
    def params(self: Self, *args, **kwargs) -> Self: ...
    def where(self, *criterion): ...
    def filter(self: Self, *criterion) -> Self: ...
    def filter_by(self: Self, **kwargs) -> Self: ...
    def order_by(self: Self, *clauses) -> Self: ...
    def group_by(self: Self, *clauses) -> Self: ...
    def having(self: Self, criterion) -> Self: ...
    def union(self, *q): ...
    def union_all(self, *q): ...
    def intersect(self, *q): ...
    def intersect_all(self, *q): ...
    def except_(self, *q): ...
    def except_all(self, *q): ...
    def join(self: Self, target, *props, **kwargs) -> Self: ...
    def outerjoin(self: Self, target, *props, **kwargs) -> Self: ...
    def reset_joinpoint(self: Self) -> Self: ...
    def select_from(self: Self, *from_obj) -> Self: ...
    def select_entity_from(self: Self, from_obj) -> Self: ...
    def __getitem__(self, item): ...
    def slice(self: Self, start, stop) -> Self: ...
    def limit(self: Self, limit) -> Self: ...
    def offset(self: Self, offset) -> Self: ...
    def distinct(self: Self, *expr) -> Self: ...
    def all(self) -> list[_T]: ...
    def from_statement(self: Self, statement) -> Self: ...
    def first(self) -> _T | None: ...
    def one_or_none(self): ...
    def one(self): ...
    def scalar(self) -> Any: ...  # type: ignore[override]
    def __iter__(self) -> Iterator[_T]: ...
    @property
    def column_descriptions(self): ...
    def instances(self, result_proxy, context: Any | None = ...): ...
    def merge_result(self, iterator, load: bool = ...): ...
    def exists(self): ...
    def count(self) -> int: ...
    def delete(self, synchronize_session: str = ...) -> int: ...
    def update(self, values, synchronize_session: str = ..., update_args: Any | None = ...): ...

class FromStatement(GroupedElement, SelectBase, Executable):
    __visit_name__: str
    element: Any
    def __init__(self, entities, element) -> None: ...
    def get_label_style(self): ...
    def set_label_style(self, label_style): ...
    def get_children(self, **kw) -> None: ...  # type: ignore[override]

class AliasOption(interfaces.LoaderOption):
    def __init__(self, alias) -> None: ...
    inherit_cache: bool
    def process_compile_state(self, compile_state) -> None: ...

class BulkUD:
    query: Any
    mapper: Any
    def __init__(self, query) -> None: ...
    @property
    def session(self): ...

class BulkUpdate(BulkUD):
    values: Any
    update_kwargs: Any
    def __init__(self, query, values, update_kwargs) -> None: ...

class BulkDelete(BulkUD): ...
