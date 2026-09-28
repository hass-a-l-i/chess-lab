import numpy as np

class BitBoard:
    def __init__(self):
        # board universe
        self.board = (1<<64)-1
        # white pieces
        self.white_rooks =  (1<<0) | (1<<7)
        self.white_knights = (1<<1) | (1<<6)
        self.white_bishops = (1<<2) |(1<<5)
        self.white_king = (1<<4)
        self.white_queen = (1<<3)
        self.white_pawns = ((1<<8)-1)<<8
        # black pieces
        self.black_rooks = (1<<56) | (1<<63)
        self.black_knights = (1<<57) | (1<<62)
        self.black_bishops = (1<<58) | (1<<61)
        self.black_king = 1<<60
        self.black_queen = 1<<59
        self.black_pawns = ((1<<8)-1)<<48

    @property
    def white_pieces(self):
        return (
            self.white_rooks 
            | self.white_knights 
            | self.white_bishops 
            | self.white_king 
            | self.white_queen 
            | self.white_pawns 
        )

    @property
    def black_pieces(self):
        return (
            self.black_rooks 
            | self.black_knights 
            | self.black_bishops 
            | self.black_king 
            | self.black_queen 
            | self.black_pawns 
        )

    @property
    def occupied(self):
        return self.white_pieces | self.black_pieces


    @property
    def free(self):
        return ~self.occupied

    
    
        
        
        
    

    