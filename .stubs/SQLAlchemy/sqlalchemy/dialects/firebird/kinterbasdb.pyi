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

from typing import Any

from ...types import Float, Numeric
from .base import FBDialect, FBExecutionContext

class _kinterbasdb_numeric:
    def bind_processor(self, dialect): ...

class _FBNumeric_kinterbasdb(_kinterbasdb_numeric, Numeric): ...
class _FBFloat_kinterbasdb(_kinterbasdb_numeric, Float): ...

class FBExecutionContext_kinterbasdb(FBExecutionContext):
    @property
    def rowcount(self): ...

class FBDialect_kinterbasdb(FBDialect):
    driver: str
    supports_statement_cache: bool
    supports_sane_rowcount: bool
    supports_sane_multi_rowcount: bool
    supports_native_decimal: bool
    colspecs: Any
    enable_rowcount: Any
    type_conv: Any
    concurrency_level: Any
    retaining: Any
    def __init__(
        self,
        type_conv: int = ...,
        concurrency_level: int = ...,
        enable_rowcount: bool = ...,
        retaining: bool = ...,
        **kwargs,
    ) -> None: ...
    @classmethod
    def dbapi(cls): ...
    def do_execute(self, cursor, statement, parameters, context: Any | None = ...) -> None: ...
    def do_rollback(self, dbapi_connection) -> None: ...
    def do_commit(self, dbapi_connection) -> None: ...
    def create_connect_args(self, url): ...
    def is_disconnect(self, e, connection, cursor): ...

dialect = FBDialect_kinterbasdb
