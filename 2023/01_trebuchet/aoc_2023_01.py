import pathlib
import string
import sys
from itertools import chain
from os import replace

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
    # Implement `find` for first_digit
    first_digit = find_first_digit(line)

    # Implement `rfind` instead for last_digit
    last_digit = find_last_digit(line)

    return int(first_digit + last_digit)


def find_first_digit(line):
    unit_indices = [
        (unit, line.find(unit))
        for number_word in NUMBER_WORDS
        for unit in number_word
        if unit in line
    ]

    sorted_combined_indices = sort_all_numbers_found(unit_indices)

    unit = sorted_combined_indices[0][0]

    return replace_number_word_with_digit(unit)


def find_last_digit(line):
    unit_indices = [
        (unit, line.rfind(unit))
        for number_word in NUMBER_WORDS
        for unit in number_word
        if unit in line
    ]

    sorted_combined_indices = sort_all_numbers_found(unit_indices)

    unit = sorted_combined_indices[-1][0]

    return replace_number_word_with_digit(unit)


def sort_all_numbers_found(*unit_indices):
    combined_indices = list(chain.from_iterable(unit_indices))

    return sorted(combined_indices, key=lambda pair: pair[1])


def replace_number_word_with_digit(unit):
    for number_word, digit in NUMBER_WORDS:
        if number_word == unit:
            return digit

    return unit


def solve_day(puzzle_input):
    data = parse_input(puzzle_input)

    solution1 = solve_part1(data)
    solution2 = solve_part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")

        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve_day(puzzle_input)

        for solution in solutions:
            print(str(solution))
