from decimal import Decimal
from typing import Any
from typing import NamedTuple

class Amount(NamedTuple):
    number: Decimal | None
    currency: str

    def to_string(self, dformat: Any = ...) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __neg__(self) -> Amount: ...
