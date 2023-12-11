import pathlib
import pytest
import advent_of_code.y2023.d02_cube_conundrum.aoc_2023_02 as aoc

PUZZLE_DIR: pathlib.Path = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> list[aoc.Game]:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def example2() -> list[aoc.Game]:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def actual_input() -> list[aoc.Game]:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1: aoc.Game) -> None:
    """Test that input is parsed properly."""
    assert example1 == [
        (
            aoc.GameId(1),
            [aoc.CubeSet(4, 0, 3), aoc.CubeSet(1, 2, 6), aoc.CubeSet(0, 2, 0)],
        ),
        (
            aoc.GameId(2),
            [aoc.CubeSet(0, 2, 1), aoc.CubeSet(1, 3, 4), aoc.CubeSet(0, 1, 1)],
        ),
        (
            aoc.GameId(3),
            [aoc.CubeSet(20, 8, 6), aoc.CubeSet(4, 13, 5), aoc.CubeSet(1, 5, 0)],
        ),
        (
            aoc.GameId(4),
            [aoc.CubeSet(3, 1, 6), aoc.CubeSet(6, 3, 0), aoc.CubeSet(14, 3, 15)],
        ),
        (aoc.GameId(5), [aoc.CubeSet(6, 3, 1), aoc.CubeSet(1, 2, 2)]),
    ]


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1: list[aoc.Game]) -> None:
    """Test part 1 on example input."""
    assert aoc.solve_part1(example1) == 8


# @pytest.mark.skip(reason="Not implemented")
def test_part1_solution(actual_input: list[aoc.Game]) -> None:
    """Test part 1 on actual solution."""
    assert aoc.solve_part1(actual_input) == 2256


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1: list[aoc.Game]) -> None:
    """Test part 2 on example input."""
    assert aoc.solve_part2(example1) == 2286


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: list[aoc.Game]) -> None:
    """Test part 2 on example input."""
    assert aoc.solve_part2(example2) == ...


# @pytest.mark.skip(reason="Not implemented")
def test_part2_solution(actual_input: list[aoc.Game]) -> None:
    """Test part 2 on actual solution."""
    assert aoc.solve_part2(actual_input) == 74229
