import pathlib
import re
import sys
from typing import Iterator, NamedTuple, Optional, Sequence


class Card(NamedTuple):
    card_id: int
    winning_numbers: Sequence[int]
    hand: Sequence[int]


def solve_day(puzzle_input: str) -> Iterator[int]:
    cards: Sequence[Card] = parse_input(puzzle_input)

    yield solve_part1(cards)
    yield solve_part2(cards)


def parse_input(puzzle_input: str) -> Sequence[Card]:
    lines: list[str] = puzzle_input.splitlines()

    return [parse_card(line) for line in lines]


def parse_card(line: str) -> Card:
    _card_id: str
    _winning_numbers: str
    _hand: str
    _card_id, _winning_numbers, _hand = parse_card_parts(line)

    card_id: int = int(_card_id)
    winning_numbers: list[int] = parse_numbers(_winning_numbers)
    hand: list[int] = parse_numbers(_hand)

    return Card(card_id, winning_numbers, hand)


def parse_card_parts(line: str) -> Iterator[str]:
    pattern: str = r"Card\s+(\d+):\s+([\d ]+) \|\s+([\d ]+)"

    card_parts: Optional[re.Match[str]] = re.match(pattern, line)

    if card_parts is None:
        raise ValueError("Line does not match expected pattern")

    yield from card_parts.groups()


def parse_numbers(line: str) -> list[int]:
    return [int(x) for x in line.split()]


def solve_part1(cards: Sequence[Card]) -> int:
    points_for_winning_cards: Sequence[int] = [get_points(card) for card in cards]

    return sum(points_for_winning_cards)


def get_points(card: Card) -> int:
    matches_count = len(get_matches(card))

    if matches_count == 0:
        return 0

    return 2 ** (matches_count - 1)


def get_matches(card: Card) -> set[int]:
    return set(card.winning_numbers).intersection(card.hand)



def solve_part2(data: Sequence[Card]) -> int:
    pass


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")

        puzzle_input: str = pathlib.Path(path).read_text().strip()
        solutions: Iterator[None] = solve_day(puzzle_input)

        for solution in solutions:
            print(str(solution))
