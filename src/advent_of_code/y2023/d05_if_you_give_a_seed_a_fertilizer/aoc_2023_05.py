# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownVariableType=false

import pathlib
import sys
from collections.abc import Generator, Iterator

from parsy import Parser, generate

from advent_of_code.utils.parsers import p_letters, p_number, symbol
from advent_of_code.y2023.d05_if_you_give_a_seed_a_fertilizer.types import (
    Almanac,
    Map,
    MapLine,
    Seed,
)


def solve_day(puzzle_input: str) -> Iterator[None]:
    data = parse_input(puzzle_input)

    yield solve_part1(data)
    yield solve_part2(data)


def parse_input(almanac: str) -> Almanac:
    result = parse_almanac.parse(almanac)

    print(result)

    return result


@generate
def parse_almanac() -> Generator[Parser, None, Almanac]:
    seeds = yield parse_seeds
    maps = yield parse_map.many()

    return Almanac(seeds, maps)  # type: ignore


@generate
def parse_seeds() -> Generator[Parser, None, set[Seed]]:
    yield symbol("seeds:")
    seeds = yield p_number.map(Seed).many()

    return set(seeds)  # type: ignore


@generate
def parse_map() -> Generator[Parser, None, Map]:
    source = yield p_letters
    yield symbol("-to-")
    destination = yield p_letters
    yield symbol("map:")
    lines = yield parse_map_line.many()

    return Map(source, destination, lines)  # type: ignore


@generate
def parse_map_line() -> Generator[Parser, None, MapLine]:
    destination_start = yield p_number
    source_start = yield p_number
    range_length = yield p_number

    return MapLine(destination_start, source_start, range_length)  # type: ignore


def solve_part1(data: Almanac):
    pass


def solve_part2(data: Almanac):
    pass


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")

        puzzle_input: str = pathlib.Path(path).read_text().strip()
        solutions: Iterator[None] = solve_day(puzzle_input)

        for solution in solutions:
            print(str(solution))
