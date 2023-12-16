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
        return (
            (self.source_start + i, self.destination_start + i)
            for i in range(self.range)
        )


@dataclass
class Map:
    source_category: Category
    destination_category: Category
    lines: Sequence[MapLine]

    @property
    def correspondences(self) -> Sequence[Correspondence]:
        return [line.correspondence for line in self.lines]

    def destination(self, source: int) -> int:
        for correspondence in self.correspondences:
            if source in correspondence.source:
                return source - correspondence.source[0] + correspondence.destination[0]
        return source

    def source(self, destination: int) -> int:
        for correspondence in self.correspondences:
            if destination in correspondence.source:
                return (
                    destination
                    - correspondence.source[0]
                    + correspondence.destination[0]
                )
        return destination


@dataclass
class Almanac:
    seeds: set[int]
    maps: Sequence[Map]
