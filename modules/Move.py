from dataclasses import dataclass


@dataclass(frozen=True)
class Move:
    piece: str
    from_sq: int
    to_sq: int
    # captured: str | None = None
    # promotion: str | None = None
    # castle
    # en passant