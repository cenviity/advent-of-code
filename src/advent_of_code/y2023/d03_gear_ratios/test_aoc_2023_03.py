import pathlib
import pytest
import advent_of_code.y2023.d03_gear_ratios.aoc_2023_03 as aoc

PUZZLE_DIR: pathlib.Path = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc.Engine:
    puzzle_input: str = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def example2() -> aoc.Engine:
    puzzle_input: str = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def actual_input() -> aoc.Engine:
    puzzle_input: str = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1: aoc.Engine) -> None:
    """Test that input is parsed properly."""
    assert example1 == [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1: aoc.Engine) -> None:
    """Test part 1 on example input."""
    assert aoc.solve_part1(example1) == 4361


# @pytest.mark.skip(reason="Not implemented")
def test_part1_solution(actual_input: aoc.Engine) -> None:
    """Test part 1 on actual solution."""
    assert aoc.solve_part1(actual_input) == 525911


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1: aoc.Engine) -> None:
    """Test part 2 on example input."""
    assert aoc.solve_part2(example1) == 467835


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: aoc.Engine) -> None:
    """Test part 2 on example input."""
    assert aoc.solve_part2(example2) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_solution(actual_input: aoc.Engine) -> None:
    """Test part 2 on actual solution."""
    assert aoc.solve_part2(actual_input) == ...
