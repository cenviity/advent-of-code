import pathlib
import sys
from collections import defaultdict

MAX_ALLOWED_CUBES = (
    12,
    13,
    14,
)


def parse_input(puzzle_input):
    lines = puzzle_input.splitlines()

    return [process_line(line) for line in lines]


def process_line(line):
    game_label, all_cube_draws = [segment.strip() for segment in line.split(":")]
    game_number = int(game_label.removeprefix("Game "))
    cube_draws = [cube_draw.strip() for cube_draw in all_cube_draws.split(";")]
    processed_cube_draws = list(map(process_cube_draw, cube_draws))

    return game_number, processed_cube_draws


def process_cube_draw(cube_draw):
    cube_sets = [cube_set.strip() for cube_set in cube_draw.split(",")]

    processed_cube_draw = defaultdict(int)

    for cube_set in cube_sets:
        cube_count, cube_colour = cube_set.split(" ")
        processed_cube_draw[cube_colour] = int(cube_count)

    return convert_dict_to_tuple(processed_cube_draw)


def convert_dict_to_tuple(cube_draw):
    red_cubes = cube_draw["red"]
    green_cubes = cube_draw["green"]
    blue_cubes = cube_draw["blue"]

    return red_cubes, green_cubes, blue_cubes


def solve_part1(games):
    possible_game_ids = [game[0] for game in games if is_possible_game(game)]

    return sum(possible_game_ids)


def is_possible_game(game):
    game_id, cube_sets = game
    red_cubes_drawn, green_cubes_drawn, blue_cubes_drawn = zip(*cube_sets)

    return (
        max(red_cubes_drawn) <= MAX_ALLOWED_CUBES[0]
        and max(green_cubes_drawn) <= MAX_ALLOWED_CUBES[1]
        and max(blue_cubes_drawn) <= MAX_ALLOWED_CUBES[2]
    )


def solve_part2(games):
    game_powers = [calculate_game_power(game) for game in games]

    return sum(game_powers)


def calculate_game_power(game):
    cube_sets = game[1]
    red_cubes_drawn, green_cubes_drawn, blue_cubes_drawn = zip(*cube_sets)

    return max(red_cubes_drawn) * max(green_cubes_drawn) * max(blue_cubes_drawn)


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
