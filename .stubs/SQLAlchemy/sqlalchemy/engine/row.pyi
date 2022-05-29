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

import abc
from collections.abc import ItemsView, KeysView, Mapping, Sequence, ValuesView
from typing import Any

from ..cresultproxy import BaseRow as BaseRow

MD_INDEX: int

def rowproxy_reconstructor(cls, state): ...

KEY_INTEGER_ONLY: int
KEY_OBJECTS_ONLY: int
KEY_OBJECTS_BUT_WARN: int
KEY_OBJECTS_NO_WARN: int

class Row(BaseRow, Sequence[Any], metaclass=abc.ABCMeta):
    @property
    def count(self): ...
    @property
    def index(self): ...
    def __contains__(self, key): ...
    __hash__: Any
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __ge__(self, other): ...
    def __gt__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def keys(self): ...

class LegacyRow(Row, metaclass=abc.ABCMeta):
    def __contains__(self, key): ...
    def has_key(self, key): ...
    def items(self): ...
    def iterkeys(self): ...
    def itervalues(self): ...
    def values(self): ...

BaseRowProxy = BaseRow
RowProxy = Row

class ROMappingView(KeysView[Any], ValuesView[Any], ItemsView[Any, Any]):
    def __init__(self, mapping, items) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __contains__(self, item): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class RowMapping(BaseRow, Mapping[Any, Any]):
    __getitem__: Any
    def __iter__(self): ...
    def __len__(self): ...
    def __contains__(self, key): ...
    def items(self): ...
    def keys(self): ...
    def values(self): ...