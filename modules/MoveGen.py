from .Move import Move
from .Board import BitBoard

class MoveGen:
    def __init__(self, board:BitBoard):
        self.board = board

    def avail_squares(self):
        for sq in range(0,64):
            shift = 1<<sq
            piece_type = self.board.white_pieces if self.board.white_move else self.board.black_pieces
            if piece_type & shift:
                yield sq

    def pawn(self):
        moves = []
        step = 8 if self.board.white_move else -8
        piece = "wP" if self.board.white_move else "bP"
        for from_sq in self.avail_squares():
            to_sq = from_sq + step
            if 0 <= to_sq < 64:
                valid_to = 1<<to_sq
                if self.board.free & valid_to:
                    moves.append(Move(piece, from_sq, to_sq))
        return moves
