# Based on https://realpython.com/python-advent-of-code/

import pathlib
import sys
from typing import Iterator


def parse_input(puzzle_input: str):
    pass


def solve_part1(data: None):
    pass


def solve_part2(data: None):
    pass


def solve_day(puzzle_input: str) -> Iterator[tuple[None, None]]:
    data = parse_input(puzzle_input)

    solution1 = solve_part1(data)
    solution2 = solve_part2(data)

    yield solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")

        puzzle_input: str = pathlib.Path(path).read_text().strip()
        solutions: Iterator[tuple[None, None]] = solve_day(puzzle_input)

        for solution in solutions:
            print(str(solution))
