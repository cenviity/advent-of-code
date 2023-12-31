import pathlib
import pytest
import advent_of_code.y2023.d01_trebuchet.aoc_2023_01 as aoc

PUZZLE_DIR: pathlib.Path = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> list[str]:
    puzzle_input: str = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def example2() -> list[str]:
    puzzle_input: str = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def actual_input() -> list[str]:
    puzzle_input: str = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1: list[str]) -> None:
    """Test that input is parsed properly."""
    assert example1 == [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1: list[str]) -> None:
    """Test part 1 on example input."""
    assert aoc.solve_part1(example1) == 142


# @pytest.mark.skip(reason="Not implemented")
def test_part1_solution(actual_input: list[str]) -> None:
    """Test part 1 on actual solution."""
    assert aoc.solve_part1(actual_input) == 55607


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1: list[str]) -> None:
    """Test part 2 on example input."""
    assert aoc.solve_part2(example1) == ...


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: list[str]) -> None:
    """Test part 2 on example input."""
    assert aoc.solve_part2(example2) == 281


# @pytest.mark.skip(reason="Not implemented")
def test_part2_solution(actual_input: list[str]) -> None:
    """Test part 2 on actual solution."""
    assert aoc.solve_part2(actual_input) == 55291
