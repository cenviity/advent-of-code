from collections.abc import Sequence
from dataclasses import dataclass
from typing import NewType

Seed = NewType("Seed", int)


@dataclass
class MapLine:
    destination_start: int
    source_start: int
    range: int


@dataclass
class Map:
    source: str
    destination: str
    lines: Sequence[MapLine]


@dataclass
class Almanac:
    seeds: set[Seed]
    maps: Sequence[Map]
