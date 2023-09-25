from Piece import Piece
class Board:
        def __init__(self) -> None:
                self.WHITE_ROOK_1 = Piece("Rook", "White", "R", 0, 0)
                self.WHITE_KNIGHT_1 = Piece("Knight", "White", "N", 0, 1)
                self.WHITE_BISHOP_1 = Piece("Bishop", "White", "B", 0, 2)
                self.WHITE_QUEEN = Piece("Queen", "White", "Q", 0, 3)
                self.WHITE_KING = Piece("King", "White", "K", 0, 4)
                self.WHITE_BISHOP_2 = Piece("Bishop", "White", "B", 0, 5)
                self.WHITE_KNIGHT_2 = Piece("Knight", "White", "N", 0, 6)
                self.WHITE_ROOK_2 = Piece("Rook", "White", "R", 0, 7)
                self.WHITE_PAWN_1 = Piece("Pawn", "White", "P", 1, 0)
                self.WHITE_PAWN_2 = Piece("Pawn", "White", "P", 1, 1)
                self.WHITE_PAWN_3 = Piece("Pawn", "White", "P", 1, 2)
                self.WHITE_PAWN_4 = Piece("Pawn", "White", "P", 1, 3)
                self.WHITE_PAWN_5 = Piece("Pawn", "White", "P", 1, 4)
                self.WHITE_PAWN_6 = Piece("Pawn", "White", "P", 1, 5)
                self.WHITE_PAWN_7 = Piece("Pawn", "White", "P", 1, 6)
                self.WHITE_PAWN_8 = Piece("Pawn", "White", "P", 1, 7)

                self.BLACK_ROOK_1 = Piece("Rook", "Black", "r", 7, 0)
                self.BLACK_KNIGHT_1 = Piece("Knight", "Black", "n", 7, 1)
                self.BLACK_BISHOP_1 = Piece("Bishop", "Black", "b", 7, 2)
                self.BLACK_QUEEN = Piece("Queen", "Black", "q", 7, 3)
                self.BLACK_KING = Piece("King", "Black", "k", 7, 4)
                self.BLACK_BISHOP_2 = Piece("Bishop", "Black", "b", 7, 5)
                self.BLACK_KNIGHT_2 = Piece("Knight", "Black", "n", 7, 6)
                self.BLACK_ROOK_2 = Piece("Rook", "Black", "r", 7, 7)
                self.BLACK_PAWN_1 = Piece("Pawn", "Black", "p", 6, 0)
                self.BLACK_PAWN_2 = Piece("Pawn", "Black", "p", 6, 1)
                self.BLACK_PAWN_3 = Piece("Pawn", "Black", "p", 6, 2)
                self.BLACK_PAWN_4 = Piece("Pawn", "Black", "p", 6, 3)
                self.BLACK_PAWN_5 = Piece("Pawn", "Black", "p", 6, 4)
                self.BLACK_PAWN_6 = Piece("Pawn", "Black", "p", 6, 5)
                self.BLACK_PAWN_7 = Piece("Pawn", "Black", "p", 6, 6)
                self.BLACK_PAWN_8 = Piece("Pawn", "Black", "p", 6, 7)
                self.EMPTY = Piece("Empty", None, " ", None, None)

                self.board = [
                        [self.WHITE_ROOK_1, self.WHITE_KNIGHT_1, self.WHITE_BISHOP_1, self.WHITE_QUEEN, self.WHITE_KING, self.WHITE_BISHOP_2, self.WHITE_KNIGHT_2, self.WHITE_ROOK_2],
                        [self.WHITE_PAWN_1, self.WHITE_PAWN_2, self.WHITE_PAWN_3, self.WHITE_PAWN_4, self.WHITE_PAWN_5, self.WHITE_PAWN_6, self.WHITE_PAWN_7, self.WHITE_PAWN_8],
                        [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
                        [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
                        [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
                        [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
                        [self.BLACK_PAWN_1, self.BLACK_PAWN_2, self.BLACK_PAWN_3, self.BLACK_PAWN_4, self.BLACK_PAWN_5, self.BLACK_PAWN_6, self.BLACK_PAWN_7, self.BLACK_PAWN_8], 
                        [self.BLACK_ROOK_1, self.BLACK_KNIGHT_1, self.BLACK_BISHOP_1, self.BLACK_QUEEN, self.BLACK_KING, self.BLACK_BISHOP_2, self.BLACK_KNIGHT_2, self.BLACK_ROOK_2]
                        ]
                


        def update_board(self, new_board):
                self.board = new_board

