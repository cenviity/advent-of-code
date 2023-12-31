import pathlib
import pytest
import advent_of_code.templates.aoc_template as aoc

PUZZLE_DIR: pathlib.Path = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> None:
    puzzle_input: str = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def example2() -> None:
    puzzle_input: str = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def actual_input() -> None:
    puzzle_input: str = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1: None) -> None:
    """Test that input is parsed properly."""
    assert example1 == ...


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1: None) -> None:
    """Test part 1 on example input."""
    assert aoc.solve_part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part1_solution(actual_input: None) -> None:
    """Test part 1 on actual solution."""
    assert aoc.solve_part1(actual_input) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1: None) -> None:
    """Test part 2 on example input."""
    assert aoc.solve_part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: None) -> None:
    """Test part 2 on example input."""
    assert aoc.solve_part2(example2) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_solution(actual_input: None) -> None:
    """Test part 2 on actual solution."""
    assert aoc.solve_part2(actual_input) == ...
