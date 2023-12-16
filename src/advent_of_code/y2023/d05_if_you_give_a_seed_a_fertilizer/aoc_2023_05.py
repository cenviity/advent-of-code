# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownVariableType=false

import pathlib
import sys
from collections.abc import Generator, Iterator
from functools import reduce

from parsy import Parser, generate

from advent_of_code.utils.parsers import p_letters, p_number, symbol
from advent_of_code.y2023.d05_if_you_give_a_seed_a_fertilizer.types import (
    Almanac,
    Category,
    Map,
    MapLine,
)


def solve_day(puzzle_input: str) -> Iterator[int]:
    data = parse_input(puzzle_input)

    yield solve_part1(data)
    yield solve_part2(data)


def parse_input(almanac: str) -> Almanac:
    result = parse_almanac.parse(almanac)

    return result


@generate
def parse_almanac() -> Generator[Parser, None, Almanac]:
    seeds = yield parse_seeds
    maps = yield parse_map.many()

    return Almanac(seeds, maps)  # type: ignore


@generate
def parse_seeds() -> Generator[Parser, None, set[int]]:
    yield symbol("seeds:")
    seeds = yield p_number.many()

    return set(seeds)  # type: ignore


@generate
def parse_map() -> Generator[Parser, None, Map]:
    source = yield p_letters
    yield symbol("-to-")
    destination = yield p_letters
    yield symbol("map:")
    lines = yield parse_map_line.many()

    return Map(Category[source], Category[destination], lines)  # type: ignore


@generate
def parse_map_line() -> Generator[Parser, None, MapLine]:
    destination_start = yield p_number
    source_start = yield p_number
    range_length = yield p_number

    return MapLine(destination_start, source_start, range_length)  # type: ignore


def solve_part1(almanac: Almanac) -> int:
    result_seeds = reduce(
        get_correspondences,
        almanac.maps,
        almanac.seeds,
    )

    return min(result_seeds)


def get_correspondences(src: set[int], map: Map) -> set[int]:
    return {map.destination(_src) for _src in src}


def solve_part2(almanac: Almanac):
    pass


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")

        puzzle_input: str = pathlib.Path(path).read_text().strip()
        solutions: Iterator[int] = solve_day(puzzle_input)

        for solution in solutions:
            print(str(solution))
