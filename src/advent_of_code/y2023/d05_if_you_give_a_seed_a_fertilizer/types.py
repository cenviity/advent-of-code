from collections.abc import Sequence
from dataclasses import dataclass
from enum import Enum


@dataclass
class Correspondence:
    source: Sequence[int]
    destination: Sequence[int]


Category = Enum(
    "Category",
    [
        "seed",
        "soil",
        "fertilizer",
        "water",
        "light",
        "temperature",
        "humidity",
        "location",
    ],
)


@dataclass
class MapLine:
    destination_start: int
    source_start: int
    range: int

    @property
    def correspondence(self) -> Correspondence:
        return Correspondence(
            range(self.source_start, self.source_start + self.range),
            range(self.destination_start, self.destination_start + self.range),
        )


@dataclass
class Map:
    source_category: Category
    destination_category: Category
    lines: Sequence[MapLine]

    @property
    def correspondences(self) -> Sequence[Correspondence]:
        return [line.correspondence for line in self.lines]

    def destination(self, src: int) -> int:
        for correspondence in self.correspondences:
            if src in correspondence.source:
                return src - correspondence.source[0] + correspondence.destination[0]
        return src

    def source(self, dst: int) -> int:
        for correspondence in self.correspondences:
            if dst in correspondence.source:
                return dst - correspondence.source[0] + correspondence.destination[0]
        return dst


@dataclass
class Almanac:
    seeds: set[int]
    maps: Sequence[Map]
