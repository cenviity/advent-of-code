from re import Match
from typing import NewType, TypeAlias

EngineLine = NewType("EngineLine", str)
Engine = NewType("Engine", list[EngineLine])
PartNumber = NewType("PartNumber", int)
StringMatch: TypeAlias = Match[str]
Cell = NewType("Cell", tuple[int, int])
