import pathlib
import sys
from string import digits


def parse_input(puzzle_input):
    return [line for line in puzzle_input.split("\n")]


def solve_part1(data):
    calibration_values = [find_first_and_last_digits(line) for line in data]

    return sum(calibration_values)


def find_first_and_last_digits(line):
    digits_only = list(filter(lambda char: is_digit(char), line))
    first_digit, last_digit = digits_only[0], digits_only[-1]
    calibration_value = int(first_digit + last_digit)

    return calibration_value


def is_digit(char):
    return char in digits


def solve_part2(data):
    calibration_values = []

    number_words = [
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

    for line in data:
        # Implement `find` for first_digit

        number_word_indices = [
            (number_word[0], line.find(number_word[0]))
            for number_word in number_words
            if number_word[0] in line
        ]

        for i, number_word_index in enumerate(number_word_indices):
            for r in number_words:
                number_word_indices[i] = (
                    number_word_indices[i][0].replace(*r),
                    number_word_indices[i][1],
                )

        digit_indices = [
            (number_word[1], line.find(number_word[1]))
            for number_word in number_words
            if number_word[1] in line
        ]

        combined_indices = number_word_indices + digit_indices

        sorted_combined_indices = sorted(combined_indices, key=lambda pair: pair[1])

        first_digit = sorted_combined_indices[0][0]

        # Implement `rfind` instead for last_digit

        number_word_indices = [
            (number_word[0], line.rfind(number_word[0]))
            for number_word in number_words
            if number_word[0] in line
        ]

        for i, number_word_index in enumerate(number_word_indices):
            for r in number_words:
                number_word_indices[i] = (
                    number_word_indices[i][0].replace(*r),
                    number_word_indices[i][1],
                )

        digit_indices = [
            (number_word[1], line.rfind(number_word[1]))
            for number_word in number_words
            if number_word[1] in line
        ]

        combined_indices = number_word_indices + digit_indices

        sorted_combined_indices = sorted(combined_indices, key=lambda pair: pair[1])

        last_digit = sorted_combined_indices[-1][0]

        calibration_value = int(first_digit + last_digit)
        calibration_values.append(calibration_value)

    return sum(calibration_values)


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
