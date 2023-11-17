from _typeshed import Incomplete, Unused
from collections.abc import Callable, Iterable, Iterator, Mapping, MutableSequence
from typing import Any, ClassVar, NamedTuple, TypeVar, overload
from typing_extensions import SupportsIndex

_S = TypeVar("_S", bound=MutableSequence[str])

def strip_blank_lines(l: _S) -> _S: ...

class Reader:
    def __init__(self, data: str | list[str]) -> None: ...
    @overload
    def __getitem__(self, n: slice) -> list[str]: ...
    @overload
    def __getitem__(self, n: SupportsIndex) -> str: ...
    def reset(self) -> None: ...
    def read(self) -> str: ...
    def seek_next_non_empty_line(self) -> None: ...
    def eof(self) -> bool: ...
    def read_to_condition(self, condition_func: Callable[[str], bool]) -> list[str]: ...
    def read_to_next_empty_line(self) -> list[str]: ...
    def read_to_next_unindented_line(self) -> list[str]: ...
    def peek(self, n: int = 0) -> str: ...
    def is_empty(self) -> bool: ...

class ParseError(Exception): ...

class Parameter(NamedTuple):
    name: str
    type: str
    desc: list[str]

class NumpyDocString(Mapping[str, Any]):
    sections: ClassVar[dict[str, Any]]
    def __init__(self, docstring: str, config: Unused = {}) -> None: ...
    def __getitem__(self, key: str) -> Any: ...
    def __setitem__(self, key: str, val: Any) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    empty_description: str

def indent(str: str | None, indent: int = 4) -> str: ...
def dedent_lines(lines: Iterable[str]) -> list[str]: ...
def header(text: str, style: str = "-") -> str: ...

class FunctionDoc(NumpyDocString):
    def __init__(self, func, role: str = "func", doc: str | None = None, config: Unused = {}) -> None: ...
    def get_func(self) -> tuple[Incomplete, str]: ...

class ClassDoc(NumpyDocString):
    extra_public_methods: list[str]
    show_inherited_members: bool
    @overload
    def __init__(
        self, cls: None, doc: str, modulename: str = "", func_doc: type[FunctionDoc] = ..., config: Mapping[str, Any] = {}
    ) -> None: ...
    @overload
    def __init__(
        self,
        cls: type,
        doc: str | None = None,
        modulename: str = "",
        func_doc: type[FunctionDoc] = ...,
        config: Mapping[str, Any] = {},
    ) -> None: ...
    @property
    def methods(self) -> list[str]: ...
    @property
    def properties(self) -> list[str]: ...