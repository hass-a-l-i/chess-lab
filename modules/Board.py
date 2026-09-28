from .Move import Move


class BitBoard:
    def __init__(self):
        # board universe
        self.board = (1<<64)-1
        # white pieces
        self.wR =  (1<<0) | (1<<7)
        self.wN = (1<<1) | (1<<6)
        self.wB = (1<<2) |(1<<5)
        self.wK = (1<<4)
        self.wQ = (1<<3)
        self.wP = ((1<<8)-1)<<8
        # black pieces
        self.bR = (1<<56) | (1<<63)
        self.bN = (1<<57) | (1<<62)
        self.bB = (1<<58) | (1<<61)
        self.bK = 1<<60
        self.bQ = 1<<59
        self.bP = ((1<<8)-1)<<48
        self.move_history = []
        self.white_move=True

    def __str__(self):
        s = ""
        s += "  ---------------------------\n"
        for rank in range(7, -1, -1):
            row = []
            for file in range(8):
                square = rank * 8 + file
                row.append(self.piece_finder(square))
            row_str = " ".join(row)
            s += f"{rank + 1} | {row_str} |\n"
        s += "  ---------------------------\n"
        s += "     a  b  c  d  e  f  g  h\n"
        return s

    @property
    def white_pieces(self):
        """bit squares occupied by white pieces"""
        return (
            self.wR
            | self.wN
            | self.wB
            | self.wK
            | self.wQ
            | self.wP
        )

    @property
    def black_pieces(self):
        """bit squares occupied by black pieces"""
        return (
            self.bR
            | self.bN
            | self.bB
            | self.bK
            | self.bQ
            | self.bP
        )

    @property
    def occupied(self):
        return self.white_pieces | self.black_pieces
        
    @property
    def free(self):
        return ~self.occupied

    def piece_finder(self, square: int):
        mask = 1<<square
        piece_names = [
            "wP", "wN", "wB", "wR", "wQ", "wK",
            "bP", "bN", "bB", "bR", "bQ", "bK"
        ]
        for piece in piece_names:
            symbol = getattr(self, piece)
            if symbol & mask:
                return piece
        return ".."

    def make_move(self, move:Move):
        piece_chosen = getattr(self, move.piece)
        from_mask = 1 << move.from_sq
        to_mask = 1 << move.to_sq
        if not (piece_chosen & from_mask):
            raise AssertionError(f"There is no white pawn on {move.from_sq}")
        piece_chosen &= ~from_mask
        piece_chosen |= to_mask
        setattr(self, move.piece, piece_chosen)
        self.move_history = [move]
        self.white_move = not self.white_move
    
        
        
        
    

    