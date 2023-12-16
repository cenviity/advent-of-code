import pathlib
from collections.abc import Sequence

import pytest

import advent_of_code.y2023.d05_if_you_give_a_seed_a_fertilizer.aoc_2023_05 as aoc
from advent_of_code.y2023.d05_if_you_give_a_seed_a_fertilizer.types import (
    Almanac,
    Category,
    Map,
    MapLine,
)

PUZZLE_DIR: pathlib.Path = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> Almanac:
    puzzle_input: str = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def example2() -> Almanac:
    puzzle_input: str = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def actual_input() -> Almanac:
    puzzle_input: str = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1: Almanac) -> None:
    """Test that input is parsed properly."""
    seeds: set[int] = {13, 55, 14, 79}
    maps: Sequence[Map] = [
        Map(
            Category.seed,
            Category.soil,
            [
                MapLine(50, 98, 2),
                MapLine(52, 50, 48),
            ],
        ),
        Map(
            Category.soil,
            Category.fertilizer,
            [
                MapLine(0, 15, 37),
                MapLine(37, 52, 2),
                MapLine(39, 0, 15),
            ],
        ),
        Map(
            Category.fertilizer,
            Category.water,
            [
                MapLine(49, 53, 8),
                MapLine(0, 11, 42),
                MapLine(42, 0, 7),
                MapLine(57, 7, 4),
            ],
        ),
        Map(
            Category.water,
            Category.light,
            [
                MapLine(88, 18, 7),
                MapLine(18, 25, 70),
            ],
        ),
        Map(
            Category.light,
            Category.temperature,
            [
                MapLine(45, 77, 23),
                MapLine(81, 45, 19),
                MapLine(68, 64, 13),
            ],
        ),
        Map(
            Category.temperature,
            Category.humidity,
            [
                MapLine(0, 69, 1),
                MapLine(1, 0, 69),
            ],
        ),
        Map(
            Category.humidity,
            Category.location,
            [
                MapLine(60, 56, 37),
                MapLine(56, 93, 4),
            ],
        ),
    ]

    almanac: Almanac = Almanac(
        seeds,
        maps,
    )

    assert example1 == almanac


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1: Almanac) -> None:
    """Test part 1 on example input."""
    assert aoc.solve_part1(example1) == 35


# @pytest.mark.skip(reason="Not implemented")
def test_part1_solution(actual_input: Almanac) -> None:
    """Test part 1 on actual solution."""
    assert aoc.solve_part1(actual_input) == 910845529


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1: Almanac) -> None:
    """Test part 2 on example input."""
    assert aoc.solve_part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: Almanac) -> None:
    """Test part 2 on example input."""
    assert aoc.solve_part2(example2) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_solution(actual_input: Almanac) -> None:
    """Test part 2 on actual solution."""
    assert aoc.solve_part2(actual_input) == ...
