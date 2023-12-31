import pathlib
import sys
from typing import Iterator, NamedTuple, NewType


class CubeSet(NamedTuple):
    red: int = 0
    green: int = 0
    blue: int = 0


GameId = NewType("GameId", int)


class Game(NamedTuple):
    game_id: GameId
    cube_sets: list[CubeSet]


MAX_ALLOWED_CUBES: CubeSet = CubeSet(
    red=12,
    green=13,
    blue=14,
)


def solve_day(puzzle_input: str) -> Iterator[int]:
    data: list[Game] = parse_input(puzzle_input)

    yield solve_part1(data)
    yield solve_part2(data)


def parse_input(puzzle_input: str) -> list[Game]:
    lines: list[str] = puzzle_input.splitlines()

    return [parse_game(line) for line in lines]


def parse_game(line: str) -> Game:
    game_label: str
    all_cube_draws: str
    game_label, all_cube_draws = [segment.strip() for segment in line.split(":")]

    game_id: GameId = GameId(int(game_label.removeprefix("Game ")))

    cube_draws: list[str] = parse_cube_draws(all_cube_draws)
    cube_sets: list[CubeSet] = list(map(parse_cubeset, cube_draws))

    return Game(game_id, cube_sets)


def parse_cube_draws(all_cube_draws: str) -> list[str]:
    return [cube_draw.strip() for cube_draw in all_cube_draws.split(";")]


def parse_cubeset(cube_draw: str) -> CubeSet:
    cube_sets: list[str] = [cube_set.strip() for cube_set in cube_draw.split(",")]

    processed_cube_draw: dict[str, int] = dict(
        parse_cube_colour_and_count(cube_set) for cube_set in cube_sets
    )

    return CubeSet(**processed_cube_draw)


def parse_cube_colour_and_count(cube_set: str) -> tuple[str, int]:
    cube_count: str
    cube_colour: str
    cube_count, cube_colour = cube_set.split(" ")

    return cube_colour, int(cube_count)


def solve_part1(games: list[Game]) -> int:
    possible_game_ids: list[GameId] = [
        game.game_id for game in games if is_possible_game(game)
    ]

    return sum(possible_game_ids)


def is_possible_game(game: Game) -> bool:
    red_cubes_drawn: tuple[int, ...]
    green_cubes_drawn: tuple[int, ...]
    blue_cubes_drawn: tuple[int, ...]
    red_cubes_drawn, green_cubes_drawn, blue_cubes_drawn = zip(*game.cube_sets)

    return (
        max(red_cubes_drawn) <= MAX_ALLOWED_CUBES.red
        and max(green_cubes_drawn) <= MAX_ALLOWED_CUBES.green
        and max(blue_cubes_drawn) <= MAX_ALLOWED_CUBES.blue
    )


def solve_part2(games: list[Game]) -> int:
    game_powers: list[int] = [calculate_game_power(game) for game in games]

    return sum(game_powers)


def calculate_game_power(game: Game) -> int:
    red_cubes_drawn: tuple[int, ...]
    green_cubes_drawn: tuple[int, ...]
    blue_cubes_drawn: tuple[int, ...]
    red_cubes_drawn, green_cubes_drawn, blue_cubes_drawn = zip(*game.cube_sets)

    return max(red_cubes_drawn) * max(green_cubes_drawn) * max(blue_cubes_drawn)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")

        puzzle_input: str = pathlib.Path(path).read_text().strip()
        solutions: Iterator[int] = solve_day(puzzle_input)

        for solution in solutions:
            print(str(solution))
