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

from sqlalchemy import sql, types as sqltypes
from sqlalchemy.engine import default
from sqlalchemy.sql import compiler
from sqlalchemy.types import (
    BIGINT as BIGINT,
    BLOB as BLOB,
    DATE as DATE,
    FLOAT as FLOAT,
    INTEGER as INTEGER,
    NUMERIC as NUMERIC,
    SMALLINT as SMALLINT,
    TEXT as TEXT,
    TIME as TIME,
    TIMESTAMP as TIMESTAMP,
    Integer as Integer,
)

RESERVED_WORDS: Any

class _StringType(sqltypes.String):
    charset: Any
    def __init__(self, charset: Any | None = ..., **kw) -> None: ...

class VARCHAR(_StringType, sqltypes.VARCHAR):
    __visit_name__: str
    def __init__(self, length: Any | None = ..., **kwargs) -> None: ...

class CHAR(_StringType, sqltypes.CHAR):
    __visit_name__: str
    def __init__(self, length: Any | None = ..., **kwargs) -> None: ...

class _FBDateTime(sqltypes.DateTime):
    def bind_processor(self, dialect): ...

colspecs: Any
ischema_names: Any

class FBTypeCompiler(compiler.GenericTypeCompiler):
    def visit_boolean(self, type_, **kw): ...
    def visit_datetime(self, type_, **kw): ...
    def visit_TEXT(self, type_, **kw): ...
    def visit_BLOB(self, type_, **kw): ...
    def visit_CHAR(self, type_, **kw): ...
    def visit_VARCHAR(self, type_, **kw): ...

class FBCompiler(sql.compiler.SQLCompiler):
    ansi_bind_rules: bool
    def visit_now_func(self, fn, **kw): ...
    def visit_startswith_op_binary(self, binary, operator, **kw): ...
    def visit_not_startswith_op_binary(self, binary, operator, **kw): ...
    def visit_mod_binary(self, binary, operator, **kw): ...
    def visit_alias(self, alias, asfrom: bool = ..., **kwargs): ...  # type: ignore[override]
    def visit_substring_func(self, func, **kw): ...
    def visit_length_func(self, function, **kw): ...
    visit_char_length_func: Any
    def function_argspec(self, func, **kw): ...
    def default_from(self): ...
    def visit_sequence(self, seq, **kw): ...
    def get_select_precolumns(self, select, **kw): ...
    def limit_clause(self, select, **kw): ...
    def returning_clause(self, stmt, returning_cols): ...

class FBDDLCompiler(sql.compiler.DDLCompiler):
    def visit_create_sequence(self, create): ...
    def visit_drop_sequence(self, drop): ...
    def visit_computed_column(self, generated): ...

class FBIdentifierPreparer(sql.compiler.IdentifierPreparer):
    reserved_words: Any
    illegal_initial_characters: Any
    def __init__(self, dialect) -> None: ...

class FBExecutionContext(default.DefaultExecutionContext):
    def fire_sequence(self, seq, type_): ...

class FBDialect(default.DefaultDialect):
    name: str
    supports_statement_cache: bool
    max_identifier_length: int
    supports_sequences: bool
    sequences_optional: bool
    supports_default_values: bool
    postfetch_lastrowid: bool
    supports_native_boolean: bool
    requires_name_normalize: bool
    supports_empty_insert: bool
    statement_compiler: Any
    ddl_compiler: Any
    preparer: Any
    type_compiler: Any
    colspecs: Any
    ischema_names: Any
    construct_arguments: Any
    def __init__(self, *args, **kwargs) -> None: ...
    implicit_returning: Any
    def initialize(self, connection) -> None: ...
    def has_table(self, connection, table_name, schema: Any | None = ...): ...  # type: ignore[override]
    def has_sequence(self, connection, sequence_name, schema: Any | None = ...): ...  # type: ignore[override]
    def get_table_names(self, connection, schema: Any | None = ..., **kw): ...
    def get_view_names(self, connection, schema: Any | None = ..., **kw): ...
    def get_view_definition(self, connection, view_name, schema: Any | None = ..., **kw): ...
    def get_pk_constraint(self, connection, table_name, schema: Any | None = ..., **kw): ...
    def get_column_sequence(
        self, connection, table_name, column_name, schema: Any | None = ..., **kw
    ): ...
    def get_columns(self, connection, table_name, schema: Any | None = ..., **kw): ...
    def get_foreign_keys(self, connection, table_name, schema: Any | None = ..., **kw): ...
    def get_indexes(self, connection, table_name, schema: Any | None = ..., **kw): ...
