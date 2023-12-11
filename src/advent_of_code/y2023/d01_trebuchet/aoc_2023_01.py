import pathlib
import string
import sys
from itertools import chain

NUMBER_WORDS = [
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


def solve_day(puzzle_input):
    data = parse_input(puzzle_input)

    yield solve_part1(data)
    yield solve_part2(data)


def parse_input(puzzle_input):
    return puzzle_input.splitlines()


def solve_part1(data):
    calibration_values = [find_first_and_last_digits(line) for line in data]

    return sum(calibration_values)


def find_first_and_last_digits(line):
    digits_only = [char for char in line if is_digit(char)]
    first_digit, last_digit = digits_only[0], digits_only[-1]
    calibration_value = int(first_digit + last_digit)

    return calibration_value


def is_digit(char):
    return char in string.digits


def solve_part2(data):
    calibration_values = [
        find_first_and_last_digits_with_numeric_words(line) for line in data
    ]

    return sum(calibration_values)


def find_first_and_last_digits_with_numeric_words(line):
    numbers_from_left = find_numbers_from_left(line)
    numbers_from_right = find_numbers_from_right(line)

    sorted_combined_indices = sorted(chain(numbers_from_left, numbers_from_right))

    first_digit = sorted_combined_indices[0][1]
    last_digit = sorted_combined_indices[-1][1]

    return int(first_digit + last_digit)


def find_numbers_from_left(line):
    for number_pair in NUMBER_WORDS:
        _, digit = number_pair

        for unit in number_pair:
            if unit in line:
                yield line.find(unit), digit


def find_numbers_from_right(line):
    for number_pair in NUMBER_WORDS:
        _, digit = number_pair

        for unit in number_pair:
            if unit in line:
                yield line.rfind(unit), digit


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")

        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve_day(puzzle_input)

        for solution in solutions:
            print(str(solution))
