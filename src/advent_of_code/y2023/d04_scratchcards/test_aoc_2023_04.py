import pathlib
import pytest
import advent_of_code.y2023.d04_scratchcards.aoc_2023_04 as aoc
from advent_of_code.y2023.d04_scratchcards.types import Card, CardId

PUZZLE_DIR: pathlib.Path = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc.Sequence[Card]:
    puzzle_input: str = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def example2() -> aoc.Sequence[Card]:
    puzzle_input: str = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def actual_input() -> aoc.Sequence[Card]:
    puzzle_input: str = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1: None) -> None:
    """Test that input is parsed properly."""
    assert example1 == [
        Card(CardId(1), [41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]),
        Card(CardId(2), [13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]),
        Card(CardId(3), [1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1]),
        Card(CardId(4), [41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83]),
        Card(CardId(5), [87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36]),
        Card(CardId(6), [31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11]),
    ]


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1: aoc.Sequence[Card]) -> None:
    """Test part 1 on example input."""
    assert aoc.solve_part1(example1) == 13


# @pytest.mark.skip(reason="Not implemented")
def test_part1_solution(actual_input: aoc.Sequence[Card]) -> None:
    """Test part 1 on actual solution."""
    assert aoc.solve_part1(actual_input) == 26443


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1: aoc.Sequence[Card]) -> None:
    """Test part 2 on example input."""
    assert aoc.solve_part2(example1) == 30


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: aoc.Sequence[Card]) -> None:
    """Test part 2 on example input."""
    assert aoc.solve_part2(example2) == ...


# @pytest.mark.skip(reason="Not implemented")
def test_part2_solution(actual_input: aoc.Sequence[Card]) -> None:
    """Test part 2 on actual solution."""
    assert aoc.solve_part2(actual_input) == 6284877
