from collections.abc import Sequence
from dataclasses import dataclass
from enum import Enum


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
class Correspondence:
    destination_start: int
    source_start: int
    range: int

    @property
    def sources(self) -> Sequence[int]:
        return range(self.source_start, self.source_start + self.range)

    @property
    def destinations(self) -> Sequence[int]:
        return range(self.destination_start, self.destination_start + self.range)


@dataclass
class Map:
    source_category: Category
    destination_category: Category
    correspondences: Sequence[Correspondence]

    def destination(self, src: int) -> int:
        for correspondence in self.correspondences:
            if src in correspondence.sources:
                return (
                    src - correspondence.source_start + correspondence.destination_start
                )
        return src

    def source(self, dst: int) -> int:
        for correspondence in self.correspondences:
            if dst in correspondence.destinations:
                return (
                    dst - correspondence.destination_start + correspondence.source_start
                )
        return dst


@dataclass
class Almanac:
    seeds: set[int]
    maps: Sequence[Map]
