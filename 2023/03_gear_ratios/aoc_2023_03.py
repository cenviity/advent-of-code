import pathlib
import re
import string
import sys


def parse_input(puzzle_input):
    return puzzle_input.splitlines()


def solve_part1(data):
    part_number_total = 0

    for line_number, line in enumerate(data):
        number_matches = find_number_matches(line)

        for number_match in number_matches:
            match_start_column = number_match.start()
            match_end_column = number_match.end() - 1
            number = int(number_match.group())

            if is_adjacent_to_symbol(
                data, line_number, match_start_column, match_end_column
            ):
                part_number_total += number

    return part_number_total


def find_number_matches(line):
    return re.finditer(r"\d+", line)


def is_adjacent_to_symbol(data, row_number, start_column, end_column):
    surrounding_coords = [
        (row_number + row_offset, i)
        for i in range(start_column - 1, end_column + 2)
        for row_offset in [-1, 1]
    ] + [(row_number, i) for i in [start_column - 1, end_column + 1]]

    return any(map(lambda coords: is_symbol(data, coords), surrounding_coords))


def is_symbol(data, coords):
    row, column = coords

    try:
        return data[row][column] not in ("." + string.digits)
    except IndexError:
        return False


def solve_part2(data):
    pass


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
