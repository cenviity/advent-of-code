import pathlib
import string
import sys
from itertools import chain
from typing import Iterator

NUMBER_WORDS: list[tuple[str, str]] = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9"),
]


def solve_day(puzzle_input: str) -> Iterator[int]:
    data: list[str] = parse_input(puzzle_input)

    yield solve_part1(data)
    yield solve_part2(data)


def parse_input(puzzle_input: str) -> list[str]:
    return puzzle_input.splitlines()


def solve_part1(data: list[str]) -> int:
    calibration_values: list[int] = [find_first_and_last_digits(line) for line in data]

    return sum(calibration_values)


def find_first_and_last_digits(line: str) -> int:
    digits_only: list[str] = [char for char in line if is_digit(char)]

    first_digit: str
    last_digit: str
    first_digit, last_digit = digits_only[0], digits_only[-1]

    return int(first_digit + last_digit)


def is_digit(char: str) -> bool:
    return char in string.digits


def solve_part2(data: list[str]) -> int:
    calibration_values: list[int] = [
        find_calibration_value_with_numeric_words(line) for line in data
    ]

    return sum(calibration_values)


def find_first_and_last_digits_with_numeric_words(line: str) -> int:
    numbers_from_left: Iterator[tuple[int, str]] = find_numbers_from_left(line)
    numbers_from_right: Iterator[tuple[int, str]] = find_numbers_from_right(line)

    sorted_combined_indices: list[tuple[int, str]] = sorted(
        chain(numbers_from_left, numbers_from_right)
    )

    first_digit: str = sorted_combined_indices[0][1]
    last_digit: str = sorted_combined_indices[-1][1]

    return int(first_digit + last_digit)


def find_numbers_from_left(line: str) -> Iterator[tuple[int, str]]:
    for number_pair in NUMBER_WORDS:
        digit: str = number_pair[1]

        for unit in number_pair:
            if unit in line:
                yield line.find(unit), digit


def find_numbers_from_right(line: str) -> Iterator[tuple[int, str]]:
    for number_pair in NUMBER_WORDS:
        digit: str = number_pair[1]

        for unit in number_pair:
            if unit in line:
                yield line.rfind(unit), digit


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")

        puzzle_input: str = pathlib.Path(path).read_text().strip()
        solutions: Iterator[int] = solve_day(puzzle_input)

        for solution in solutions:
            print(str(solution))
