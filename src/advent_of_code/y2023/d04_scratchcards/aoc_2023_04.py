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
    _line: Optional[re.Match[str]] = parse_line(line)

    assert _line is not None

    _card_id: str
    _winning_numbers: str
    _hand: str
    _card_id, _winning_numbers, _hand = _line.groups()

    card_id: int = int(_card_id)
    winning_numbers = [int(x) for x in re.split(r"\s+", _winning_numbers)]
    hand = [int(x) for x in re.split(r"\s+", _hand)]

    return Card(card_id, winning_numbers, hand)


def parse_line(line: str) -> Optional[re.Match[str]]:
    pattern: str = r"Card\s+(\d+):\s+([\d ]+) \|\s+([\d ]+)"

    return re.match(pattern, line)


def solve_part1(cards: Sequence[Card]) -> int:
    points_for_winning_cards: Sequence[int] = [get_points(card) for card in cards]

    return sum(points_for_winning_cards)


def get_points(card: Card) -> int:
    winning_numbers_in_hand: set[int] = set(card.winning_numbers).intersection(
        card.hand
    )

    winning_numbers_in_hand_count: int = len(winning_numbers_in_hand)

    if winning_numbers_in_hand_count == 0:
        return 0
    else:
        return 2 ** (winning_numbers_in_hand_count - 1)


def solve_part2(data: Sequence[Card]) -> int:
    pass


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")

        puzzle_input: str = pathlib.Path(path).read_text().strip()
        solutions: Iterator[None] = solve_day(puzzle_input)

        for solution in solutions:
            print(str(solution))
