import pathlib
import pytest
import aoc_2023_02 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def actual_input():
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        (1, [(4, 0, 3), (1, 2, 6), (0, 2, 0)]),
        (2, [(0, 2, 1), (1, 3, 4), (0, 1, 1)]),
        (3, [(20, 8, 6), (4, 13, 5), (1, 5, 0)]),
        (4, [(3, 1, 6), (6, 3, 0), (14, 3, 15)]),
        (5, [(6, 3, 1), (1, 2, 2)]),
    ]


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.solve_part1(example1) == 8


# @pytest.mark.skip(reason="Not implemented")
def test_part1_solution(actual_input):
    """Test part 1 on actual solution."""
    assert aoc.solve_part1(actual_input) == 2256


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.solve_part2(example1) == 2286


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.solve_part2(example2) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_solution(actual_input):
    """Test part 2 on actual solution."""
    assert aoc.solve_part2(actual_input) == ...
