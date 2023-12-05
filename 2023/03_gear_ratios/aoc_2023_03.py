import itertools
import pathlib
import re
import string
import sys


def parse_input(puzzle_input):
    return puzzle_input.splitlines()


def solve_part1(engine):
    all_part_numbers = (
        part_number
        for line_of_part_numbers in get_part_numbers(engine)
        for part_number in line_of_part_numbers
    )

    return sum(all_part_numbers)


def get_part_numbers(engine):
    return (
        get_part_numbers_in_line(engine, line_number, line)
        for line_number, line in enumerate(engine)
    )


def get_part_numbers_in_line(engine, line_number, line):
    number_matches = re.finditer(r"\d+", line)

    part_numbers = (
        extract_number_from_match(number_match)
        for number_match in number_matches
        if is_adjacent_to_symbol(engine, line_number, number_match)
    )

    return part_numbers


def extract_number_from_match(number_match):
    return int(number_match.group())


def is_adjacent_to_symbol(engine, row, number_match):
    start_column = number_match.start()
    end_column = number_match.end() - 1

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
