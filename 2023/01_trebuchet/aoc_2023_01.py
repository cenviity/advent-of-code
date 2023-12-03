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
    numbers_from_left = find_numbers_from_left(line)
    numbers_from_right = find_numbers_from_right(line)

    sorted_combined_indices = sort_all_numbers_found(
        numbers_from_left + numbers_from_right
    )

    first_number = sorted_combined_indices[0][1]
    last_number = sorted_combined_indices[-1][1]

    first_digit = replace_number_word_with_digit(first_number)
    last_digit = replace_number_word_with_digit(last_number)

    return int(first_digit + last_digit)


def find_numbers_from_left(line):
    return [
        (line.find(unit), unit)
        for number_word in NUMBER_WORDS
        for unit in number_word
        if unit in line
    ]


def find_numbers_from_right(line):
    return [
        (line.rfind(unit), unit)
        for number_word in NUMBER_WORDS
        for unit in number_word
        if unit in line
    ]


def sort_all_numbers_found(unit_indices):
    return sorted(unit_indices)


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
