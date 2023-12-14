import pathlib

import pytest

import advent_of_code.y2023.d02_cube_conundrum.aoc_2023_02 as aoc
from advent_of_code.y2023.d02_cube_conundrum.types import CubeSet, Game, GameId

PUZZLE_DIR: pathlib.Path = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> list[Game]:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def example2() -> list[Game]:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def actual_input() -> list[Game]:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1: Game) -> None:
    """Test that input is parsed properly."""
    assert example1 == [
        (
            GameId(1),
            [CubeSet(4, 0, 3), CubeSet(1, 2, 6), CubeSet(0, 2, 0)],
        ),
        (
            GameId(2),
            [CubeSet(0, 2, 1), CubeSet(1, 3, 4), CubeSet(0, 1, 1)],
        ),
        (
            GameId(3),
            [CubeSet(20, 8, 6), CubeSet(4, 13, 5), CubeSet(1, 5, 0)],
        ),
        (
            GameId(4),
            [CubeSet(3, 1, 6), CubeSet(6, 3, 0), CubeSet(14, 3, 15)],
        ),
        (GameId(5), [CubeSet(6, 3, 1), CubeSet(1, 2, 2)]),
    ]


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1: list[Game]) -> None:
    """Test part 1 on example input."""
    assert aoc.solve_part1(example1) == 8


# @pytest.mark.skip(reason="Not implemented")
def test_part1_solution(actual_input: list[Game]) -> None:
    """Test part 1 on actual solution."""
    assert aoc.solve_part1(actual_input) == 2256


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1: list[Game]) -> None:
    """Test part 2 on example input."""
    assert aoc.solve_part2(example1) == 2286


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: list[Game]) -> None:
    """Test part 2 on example input."""
    assert aoc.solve_part2(example2) == ...


# @pytest.mark.skip(reason="Not implemented")
def test_part2_solution(actual_input: list[Game]) -> None:
    """Test part 2 on actual solution."""
    assert aoc.solve_part2(actual_input) == 74229
