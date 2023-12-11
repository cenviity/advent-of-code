# Based on https://realpython.com/python-advent-of-code/

import pathlib
import sys
from typing import Iterator


def solve_day(puzzle_input: str) -> Iterator[None]:
    data = parse_input(puzzle_input)

    yield solve_part1(data)
    yield solve_part2(data)


def parse_input(puzzle_input: str):
    pass


def solve_part1(data: None):
    pass


def solve_part2(data: None):
    pass


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")

        puzzle_input: str = pathlib.Path(path).read_text().strip()
        solutions: Iterator[None] = solve_day(puzzle_input)

        for solution in solutions:
            print(str(solution))
