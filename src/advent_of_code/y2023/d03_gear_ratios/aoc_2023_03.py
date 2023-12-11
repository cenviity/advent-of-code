import itertools
import math
import pathlib
import re
import string
import sys
from typing import Iterator, NewType, TypeAlias

EngineLine = NewType("EngineLine", str)
Engine = NewType("Engine", list[EngineLine])
PartNumber = NewType("PartNumber", int)
StringMatch: TypeAlias = re.Match[str]
Cell = NewType("Cell", tuple[int, int])


def solve_day(puzzle_input: str) -> Iterator[int]:
    data: Engine = parse_input(puzzle_input)

    yield solve_part1(data)
    yield solve_part2(data)


def parse_input(puzzle_input: str) -> Engine:
    return Engine(list(map(EngineLine, puzzle_input.splitlines())))


def solve_part1(engine: Engine) -> int:
    all_part_numbers: Iterator[PartNumber] = (
        part_number
        for line_of_part_numbers in get_part_numbers(engine)
        for part_number in line_of_part_numbers
    )

    return sum(all_part_numbers)


def get_part_numbers(
    engine: Engine,
) -> Iterator[Iterator[PartNumber]]:
    return (
        get_part_numbers_in_line(engine, line_number, line)
        for line_number, line in enumerate(engine)
    )


def get_part_numbers_in_line(
    engine: Engine, line_number: int, line: EngineLine
) -> Iterator[PartNumber]:
    number_matches: Iterator[StringMatch] = re.finditer(r"\d+", line)

    return (
        PartNumber(extract_number_from_match(number_match))
        for number_match in number_matches
        if is_adjacent_to_symbol(engine, line_number, number_match)
    )


def extract_number_from_match(number_match: StringMatch) -> int:
    return int(number_match.group())


def is_adjacent_to_symbol(engine: Engine, row: int, number_match: StringMatch) -> bool:
    start_column: int = number_match.start()
    end_column: int = number_match.end()

    cells_above_and_below: Iterator[Cell] = (
        Cell((row + row_offset, column))
        for row_offset in [-1, 1]
        for column in range(start_column - 1, end_column + 1)
    )

    cells_left_and_right: Iterator[Cell] = (
        Cell((row, column)) for column in [start_column - 1, end_column]
    )

    surrounding_cells: itertools.chain[Cell] = itertools.chain(
        cells_above_and_below,
        cells_left_and_right,
    )

    return any(is_symbol(engine, cell) for cell in surrounding_cells)


def is_symbol(engine: Engine, cell: Cell) -> bool:
    row: int
    column: int
    row, column = cell

    try:
        return engine[row][column] not in ("." + string.digits)
    except IndexError:
        return False


def solve_part2(engine: Engine) -> int:
    gears: Iterator[Iterator[Iterator[PartNumber]]] = get_gears(engine)

    gear_ratios: list[int] = [
        get_gear_ratio(part_numbers)
        for part_numbers_list in gears
        for part_numbers in part_numbers_list
    ]

    return sum(gear_ratios)


def get_gears(engine: Engine) -> Iterator[Iterator[Iterator[PartNumber]]]:
    return (
        get_gears_in_line(engine, line_number, line)
        for line_number, line in enumerate(engine)
    )


def get_gears_in_line(
    engine: Engine, line_number: int, line: EngineLine
) -> Iterator[Iterator[PartNumber]]:
    symbol_matches: Iterator[StringMatch] = re.finditer(r"[^\d\.]", line)

    return (
        get_adjacent_part_numbers(engine, line_number, symbol_match)
        for symbol_match in symbol_matches
        if is_gear(engine, line_number, symbol_match)
    )


def is_gear(engine: Engine, line_number: int, symbol_match: StringMatch) -> bool:
    adjacent_part_numbers: Iterator[PartNumber] = get_adjacent_part_numbers(
        engine, line_number, symbol_match
    )

    return len(list(adjacent_part_numbers)) == 2


def get_adjacent_part_numbers(
    engine: Engine, line_number: int, symbol_match: StringMatch
) -> Iterator[PartNumber]:
    start_column: int = symbol_match.start()
    end_column: int = symbol_match.end()

    number_matches_in_line_above: Iterator[StringMatch]
    number_matches_in_line_above = get_number_matches_in_line(engine[line_number - 1])
    number_matches_in_current_line: Iterator[StringMatch]
    number_matches_in_current_line = get_number_matches_in_line(engine[line_number])
    number_matches_in_line_below: Iterator[StringMatch]
    number_matches_in_line_below = get_number_matches_in_line(engine[line_number + 1])

    number_matches: itertools.chain[StringMatch] = itertools.chain(
        number_matches_in_line_above,
        number_matches_in_current_line,
        number_matches_in_line_below,
    )

    return (
        PartNumber(extract_number_from_match(number_match))
        for number_match in number_matches
        if number_match.end() - 1 in range(start_column - 1, end_column + 1)
        or number_match.start() in range(start_column - 1, end_column + 1)
    )


def get_number_matches_in_line(line: EngineLine) -> Iterator[StringMatch]:
    return re.finditer(r"\d+", line)


def get_gear_ratio(part_numbers: Iterator[PartNumber]) -> int:
    return math.prod(part_numbers)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")

        puzzle_input: str = pathlib.Path(path).read_text().strip()
        solutions: Iterator[int] = solve_day(puzzle_input)

        for solution in solutions:
            print(str(solution))
