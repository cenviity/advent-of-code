from collections import Counter
from dataclasses import dataclass
from functools import reduce
import pathlib
import re
import sys
from typing import Iterator, Optional, Sequence


@dataclass
class Card:
    card_id: int
    winning_numbers: Sequence[int]
    hand: Sequence[int]

    @property
    def matches(self) -> set[int]:
        return set(self.winning_numbers).intersection(self.hand)

    @property
    def matches_count(self) -> int:
        return len(self.matches)

    @property
    def points(self) -> int:
        if self.matches_count == 0:
            return 0

        return 2 ** (self.matches_count - 1)

    @property
    def unique_cards_won(self) -> Sequence[int]:
        return range(self.card_id + 1, self.card_id + self.matches_count + 1)


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
    points_for_winning_cards: Sequence[int] = [card.points for card in cards]

    return sum(points_for_winning_cards)


def solve_part2(cards: Sequence[Card]) -> int:
    initial_card_counts: Counter[int] = Counter({card.card_id: 1 for card in cards})
    card_counts: Counter[int] = reduce(update_card_counts, cards, initial_card_counts)

    return sum(card_counts.values())


def update_card_counts(card_counts: Counter[int], card: Card) -> Counter[int]:
    return card_counts + Counter(
        {
            unique_card_won: card_counts[card.card_id]
            for unique_card_won in card.unique_cards_won
        }
    )


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")

        puzzle_input: str = pathlib.Path(path).read_text().strip()
        solutions: Iterator[int] = solve_day(puzzle_input)

        for solution in solutions:
            print(str(solution))
