import pathlib
import sys
from collections import defaultdict
from typing import Iterator, NamedTuple, NewType


class CubeSet(NamedTuple):
    red: int = 0
    green: int = 0
    blue: int = 0


GameId = NewType("GameId", int)

MAX_ALLOWED_CUBES: CubeSet = CubeSet(
    red=12,
    green=13,
    blue=14,
)


def parse_input(puzzle_input: str) -> list[tuple[GameId, list[CubeSet]]]:
    lines: list[str] = puzzle_input.splitlines()

    return [extract_gameid_and_cubesets(line) for line in lines]


def extract_gameid_and_cubesets(line: str) -> tuple[GameId, list[CubeSet]]:
    game_label: str
    all_cube_draws: str
    game_label, all_cube_draws = [segment.strip() for segment in line.split(":")]

    game_id: GameId = GameId(int(game_label.removeprefix("Game ")))
    cube_draws: list[str] = [
        cube_draw.strip() for cube_draw in all_cube_draws.split(";")
    ]
    processed_cube_draws: list[CubeSet] = list(map(process_cube_draw, cube_draws))

    return game_id, processed_cube_draws


def process_cube_draw(cube_draw: str) -> CubeSet:
    cube_sets: list[str] = [cube_set.strip() for cube_set in cube_draw.split(",")]

    processed_cube_draw: defaultdict[str, int] = defaultdict(int)

    for cube_set in cube_sets:
        cube_count: str
        cube_colour: str
        cube_count, cube_colour = cube_set.split(" ")

        processed_cube_draw[cube_colour] = int(cube_count)

    return convert_dict_to_cubeset(processed_cube_draw)


def convert_dict_to_cubeset(cube_draw: defaultdict[str, int]) -> CubeSet:
    red_cubes: int = cube_draw["red"]
    green_cubes: int = cube_draw["green"]
    blue_cubes: int = cube_draw["blue"]

    return CubeSet(red_cubes, green_cubes, blue_cubes)


def solve_part1(games: list[tuple[GameId, list[CubeSet]]]) -> int:
    possible_game_ids: list[GameId] = [
        game[0] for game in games if is_possible_game(game)
    ]

    return sum(possible_game_ids)


def is_possible_game(game: tuple[GameId, list[CubeSet]]) -> bool:
    cube_sets: list[CubeSet] = game[1]

    red_cubes_drawn: CubeSet
    green_cubes_drawn: CubeSet
    blue_cubes_drawn: CubeSet
    red_cubes_drawn, green_cubes_drawn, blue_cubes_drawn = zip(*cube_sets)

    return (
        max(red_cubes_drawn) <= MAX_ALLOWED_CUBES[0]
        and max(green_cubes_drawn) <= MAX_ALLOWED_CUBES[1]
        and max(blue_cubes_drawn) <= MAX_ALLOWED_CUBES[2]
    )


def solve_part2(games: list[tuple[GameId, list[CubeSet]]]) -> int:
    game_powers: list[int] = [calculate_game_power(game) for game in games]

    return sum(game_powers)


def calculate_game_power(game: tuple[GameId, list[CubeSet]]) -> int:
    cube_sets: list[CubeSet] = game[1]

    red_cubes_drawn: CubeSet
    green_cubes_drawn: CubeSet
    blue_cubes_drawn: CubeSet
    red_cubes_drawn, green_cubes_drawn, blue_cubes_drawn = zip(*cube_sets)

    return max(red_cubes_drawn) * max(green_cubes_drawn) * max(blue_cubes_drawn)


def solve_day(puzzle_input: str) -> Iterator[int]:
    data: list[tuple[GameId, list[CubeSet]]] = parse_input(puzzle_input)

    solution1: int = solve_part1(data)
    solution2: int = solve_part2(data)

    yield solution1
    yield solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")

        puzzle_input: str = pathlib.Path(path).read_text().strip()
        solutions: Iterator[int] = solve_day(puzzle_input)

        for solution in solutions:
            print(str(solution))
