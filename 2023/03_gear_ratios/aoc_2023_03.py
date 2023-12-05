import itertools
import pathlib
import re
import string
import sys


def parse_input(puzzle_input):
    return puzzle_input.splitlines()


def solve_part1(engine):
    part_numbers_by_line = (
        get_part_numbers(engine, line_number, line)
        for line_number, line in enumerate(engine)
    )

    all_part_numbers = (
        part_number
        for line_of_part_numbers in part_numbers_by_line
        for part_number in line_of_part_numbers
    )

    return sum(all_part_numbers)


def get_part_numbers(engine, line_number, line):
    result = []
    number_matches = find_number_matches(line)

    for number_match in number_matches:
        match_start_column = number_match.start()
        match_end_column = number_match.end() - 1
        matched_number = int(number_match.group())

        if is_adjacent_to_symbol(
            engine, line_number, match_start_column, match_end_column
        ):
            result.append(matched_number)

    return result


def find_number_matches(line):
    return re.finditer(r"\d+", line)


def is_adjacent_to_symbol(engine, row, start_column, end_column):
    cells_above_and_below = (
        (row + row_offset, column)
        for row_offset in [-1, 1]
        for column in range(start_column - 1, end_column + 2)
    )

    cells_left_and_right = (
        (row, column) for column in [start_column - 1, end_column + 1]
    )

    surrounding_cells = itertools.chain(
        cells_above_and_below,
        cells_left_and_right,
    )

    return any(is_symbol(engine, cell) for cell in surrounding_cells)


def is_symbol(engine, cell):
    row, column = cell

    try:
        return engine[row][column] not in ("." + string.digits)
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
