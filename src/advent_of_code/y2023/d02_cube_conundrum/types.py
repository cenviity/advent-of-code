from typing import NamedTuple, NewType


class CubeSet(NamedTuple):
    red: int = 0
    green: int = 0
    blue: int = 0


GameId = NewType("GameId", int)


class Game(NamedTuple):
    game_id: GameId
    cube_sets: list[CubeSet]
