from os import replace
import pathlib
import string
import sys

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
    number_word_indices = [
        (number_word[0], line.find(number_word[0]))
        for number_word in NUMBER_WORDS
        if number_word[0] in line
    ]

    replace_number_word_with_digit(number_word_indices)

    digit_indices = [
        (number_word[1], line.find(number_word[1]))
        for number_word in NUMBER_WORDS
        if number_word[1] in line
    ]

    combined_indices = number_word_indices + digit_indices

    sorted_combined_indices = sorted(combined_indices, key=lambda pair: pair[1])

    return sorted_combined_indices[0][0]


def find_last_digit(line):
    number_word_indices = [
        (number_word[0], line.rfind(number_word[0]))
        for number_word in NUMBER_WORDS
        if number_word[0] in line
    ]

    replace_number_word_with_digit(number_word_indices)

    digit_indices = [
        (number_word[1], line.rfind(number_word[1]))
        for number_word in NUMBER_WORDS
        if number_word[1] in line
    ]

    combined_indices = number_word_indices + digit_indices

    sorted_combined_indices = sorted(combined_indices, key=lambda pair: pair[1])

    return sorted_combined_indices[-1][0]


def replace_number_word_with_digit(number_word_indices):
    for i, _ in enumerate(number_word_indices):
        for r in NUMBER_WORDS:
            number_word_indices[i] = (
                number_word_indices[i][0].replace(*r),
                number_word_indices[i][1],
            )


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
