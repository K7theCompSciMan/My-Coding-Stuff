from Piece import Piece
class Board:
        def __init__(self) -> None:
                self.board = [
                [BLACK_ROOK_1, BLACK_KNIGHT_1, BLACK_BISHOP_1, BLACK_QUEEN, BLACK_KING, BLACK_BISHOP_2, BLACK_KNIGHT_2, BLACK_ROOK_2],    
                [BLACK_PAWN_1, BLACK_PAWN_2, BLACK_PAWN_3, BLACK_PAWN_4, BLACK_PAWN_5, BLACK_PAWN_6, BLACK_PAWN_7, BLACK_PAWN_8],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [WHITE_PAWN_1, WHITE_PAWN_2, WHITE_PAWN_3, WHITE_PAWN_4, WHITE_PAWN_5, WHITE_PAWN_6, WHITE_PAWN_7, WHITE_PAWN_8],
                [WHITE_ROOK_1, WHITE_KNIGHT_1, WHITE_BISHOP_1, WHITE_QUEEN, WHITE_KING, WHITE_BISHOP_2, WHITE_KNIGHT_2, WHITE_ROOK_2]
                ]
        WHITE_ROOK_1 = Piece("Rook", "White", "R", 0, 0)
        WHITE_KNIGHT_1 = Piece("Knight", "White", "N", 0, 1)
        WHITE_BISHOP_1 = Piece("Bishop", "White", "B", 0, 2)
        WHITE_QUEEN = Piece("Queen", "White", "Q", 0, 3)
        WHITE_KING = Piece("King", "White", "K", 0, 4)
        WHITE_BISHOP_2 = Piece("Bishop", "White", "B", 0, 5)
        WHITE_KNIGHT_2 = Piece("Knight", "White", "N", 0, 6)
        WHITE_ROOK_2 = Piece("Rook", "White", "R", 0, 7)
        WHITE_PAWN_1 = Piece("Pawn", "White", "P", 1, 0)
        WHITE_PAWN_2 = Piece("Pawn", "White", "P", 1, 1)
        WHITE_PAWN_3 = Piece("Pawn", "White", "P", 1, 2)
        WHITE_PAWN_4 = Piece("Pawn", "White", "P", 1, 3)
        WHITE_PAWN_5 = Piece("Pawn", "White", "P", 1, 4)
        WHITE_PAWN_6 = Piece("Pawn", "White", "P", 1, 5)
        WHITE_PAWN_7 = Piece("Pawn", "White", "P", 1, 6)
        WHITE_PAWN_8 = Piece("Pawn", "White", "P", 1, 7)

        BLACK_ROOK_1 = Piece("Rook", "Black", "r", 7, 0)
        BLACK_KNIGHT_1 = Piece("Knight", "Black", "n", 7, 1)
        BLACK_BISHOP_1 = Piece("Bishop", "Black", "b", 7, 2)
        BLACK_QUEEN = Piece("Queen", "Black", "q", 7, 3)
        BLACK_KING = Piece("King", "Black", "k", 7, 4)
        BLACK_BISHOP_2 = Piece("Bishop", "Black", "b", 7, 5)
        BLACK_KNIGHT_2 = Piece("Knight", "Black", "n", 7, 6)
        BLACK_ROOK_2 = Piece("Rook", "Black", "r", 7, 7)
        BLACK_PAWN_1 = Piece("Pawn", "Black", "p", 6, 0)
        BLACK_PAWN_2 = Piece("Pawn", "Black", "p", 6, 1)
        BLACK_PAWN_3 = Piece("Pawn", "Black", "p", 6, 2)
        BLACK_PAWN_4 = Piece("Pawn", "Black", "p", 6, 3)
        BLACK_PAWN_5 = Piece("Pawn", "Black", "p", 6, 4)
        BLACK_PAWN_6 = Piece("Pawn", "Black", "p", 6, 5)
        BLACK_PAWN_7 = Piece("Pawn", "Black", "p", 6, 6)
        BLACK_PAWN_8 = Piece("Pawn", "Black", "p", 6, 7)



        def update_board(self, new_board):
                self.board = new_board
        


