# Based on https://realpython.com/python-advent-of-code/

import pathlib
import sys


def parse_input(puzzle_input):
    pass


def solve_part1(data):
    pass


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
