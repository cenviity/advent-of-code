# pyright: reportMissingTypeStubs = false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownVariableType=false

import functools
import pathlib
import sys
from collections import Counter
from typing import Generator, Iterator, Sequence

from parsy import generate

from advent_of_code.y2023.d04_scratchcards.parsers import Parser, p_number, symbol
from advent_of_code.y2023.d04_scratchcards.types import Card, CardId


def solve_day(puzzle_input: str) -> Iterator[int]:
    cards: Sequence[Card] = parse_input(puzzle_input)

    yield solve_part1(cards)
    yield solve_part2(cards)


def parse_input(puzzle_input: str) -> Sequence[Card]:
    lines: list[str] = puzzle_input.splitlines()

    return [parse_card.parse(line) for line in lines]


@generate
def parse_card() -> Generator[Parser, None, Card]:
    yield symbol("Card")
    card_id = yield p_number.map(int).map(CardId)
    yield symbol(":")
    winning_numbers = yield p_number.many()
    yield symbol("|")
    hand = yield p_number.many()

    return Card(card_id, winning_numbers, hand)  # type: ignore


def solve_part1(cards: Sequence[Card]) -> int:
    points_for_winning_cards: Sequence[int] = [card.points for card in cards]

    return sum(points_for_winning_cards)


def solve_part2(cards: Sequence[Card]) -> int:
    initial_card_counts: Counter[CardId] = Counter({card.card_id: 1 for card in cards})
    card_counts: Counter[CardId] = functools.reduce(
        update_card_counts, cards, initial_card_counts
    )

    return card_counts.total()


def update_card_counts(card_counts: Counter[CardId], card: Card) -> Counter[CardId]:
    card_copies: int = card_counts[card.card_id]
    cards_won: Iterator[CardId] = card.unique_cards_won

    return card_counts + count_cards_won(card_copies, cards_won)


def count_cards_won(card_copies: int, cards_won: Iterator[CardId]) -> Counter[CardId]:
    return Counter({card_won: card_copies for card_won in cards_won})


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")

        puzzle_input: str = pathlib.Path(path).read_text().strip()
        solutions: Iterator[int] = solve_day(puzzle_input)

        for solution in solutions:
            print(str(solution))
