from dataclasses import dataclass
from typing import Iterator, NewType, Sequence

CardId = NewType("CardId", int)


@dataclass
class Card:
    card_id: CardId
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
    def unique_cards_won(self) -> Iterator[CardId]:
        return map(
            CardId, range(self.card_id + 1, self.card_id + self.matches_count + 1)
        )
