import pathlib
from collections.abc import Sequence

import pytest

import advent_of_code.y2023.d05_if_you_give_a_seed_a_fertilizer.aoc_2023_05 as aoc
from advent_of_code.y2023.d05_if_you_give_a_seed_a_fertilizer.types import (
    Almanac,
    Category,
    Correspondence,
    Map,
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
                Correspondence(50, 98, 2),
                Correspondence(52, 50, 48),
            ],
        ),
        Map(
            Category.soil,
            Category.fertilizer,
            [
                Correspondence(0, 15, 37),
                Correspondence(37, 52, 2),
                Correspondence(39, 0, 15),
            ],
        ),
        Map(
            Category.fertilizer,
            Category.water,
            [
                Correspondence(49, 53, 8),
                Correspondence(0, 11, 42),
                Correspondence(42, 0, 7),
                Correspondence(57, 7, 4),
            ],
        ),
        Map(
            Category.water,
            Category.light,
            [
                Correspondence(88, 18, 7),
                Correspondence(18, 25, 70),
            ],
        ),
        Map(
            Category.light,
            Category.temperature,
            [
                Correspondence(45, 77, 23),
                Correspondence(81, 45, 19),
                Correspondence(68, 64, 13),
            ],
        ),
        Map(
            Category.temperature,
            Category.humidity,
            [
                Correspondence(0, 69, 1),
                Correspondence(1, 0, 69),
            ],
        ),
        Map(
            Category.humidity,
            Category.location,
            [
                Correspondence(60, 56, 37),
                Correspondence(56, 93, 4),
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


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1: Almanac) -> None:
    """Test part 2 on example input."""
    assert aoc.solve_part2(example1) == 46


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: Almanac) -> None:
    """Test part 2 on example input."""
    assert aoc.solve_part2(example2) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_solution(actual_input: Almanac) -> None:
    """Test part 2 on actual solution."""
    assert aoc.solve_part2(actual_input) == ...
