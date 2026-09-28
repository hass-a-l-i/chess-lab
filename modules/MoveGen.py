from dataclasses import dataclass


@dataclass(frozen=True)
class Moves:
    from_square: int
    to_square: int
    piece: str