import os
import pygame as p
from Piece import Piece


class Board:
    def __init__(self, image_width, image_height) -> None:
        self.WIDTH = image_width
        self.HEIGHT = image_height
        self.WHITE_ROOK_1 = Piece("Rook", "White", "R", 0, 0, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_rook.png")), (self.WIDTH, self.HEIGHT)), 5, self)
        self.WHITE_KNIGHT_1 = Piece("Knight", "White", "N", 0, 1, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_knight.png")), (self.WIDTH, self.HEIGHT)), 3, self)
        self.WHITE_BISHOP_1 = Piece("Bishop", "White", "B", 0, 2, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_bishop.png")), (self.WIDTH, self.HEIGHT)), 3.5, self)
        self.WHITE_QUEEN = Piece("Queen", "White", "Q", 0, 3, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_queen.png")), (self.WIDTH, self.HEIGHT)), 9, self)
        self.WHITE_KING = Piece("King", "White", "K", 0, 4, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_king.png")), (self.WIDTH, self.HEIGHT)), 100, self)
        self.WHITE_BISHOP_2 = Piece("Bishop", "White", "B", 0, 5, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_bishop.png")), (self.WIDTH, self.HEIGHT)), 3.5, self)
        self.WHITE_KNIGHT_2 = Piece("Knight", "White", "N", 0, 6, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_knight.png")), (self.WIDTH, self.HEIGHT)), 3, self)
        self.WHITE_ROOK_2 = Piece("Rook", "White", "R", 0, 7, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_rook.png")), (self.WIDTH, self.HEIGHT)), 5, self)
        self.WHITE_PAWN_1 = Piece("Pawn", "White", "P", 1, 0, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_pawn.png")), (self.WIDTH, self.HEIGHT)), 1, self)
        self.WHITE_PAWN_2 = Piece("Pawn", "White", "P", 1, 1, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_pawn.png")), (self.WIDTH, self.HEIGHT)), 1, self)
        self.WHITE_PAWN_3 = Piece("Pawn", "White", "P", 1, 2, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_pawn.png")), (self.WIDTH, self.HEIGHT)), 1, self)
        self.WHITE_PAWN_4 = Piece("Pawn", "White", "P", 1, 3, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_pawn.png")), (self.WIDTH, self.HEIGHT)), 1, self)
        self.WHITE_PAWN_5 = Piece("Pawn", "White", "P", 1, 4, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_pawn.png")), (self.WIDTH, self.HEIGHT)), 1, self)
        self.WHITE_PAWN_6 = Piece("Pawn", "White", "P", 1, 5, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_pawn.png")), (self.WIDTH, self.HEIGHT)), 1, self)
        self.WHITE_PAWN_7 = Piece("Pawn", "White", "P", 1, 6, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_pawn.png")), (self.WIDTH, self.HEIGHT)), 1, self)
        self.WHITE_PAWN_8 = Piece("Pawn", "White", "P", 1, 7, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_pawn.png")), (self.WIDTH, self.HEIGHT)), 1, self)

        self.BLACK_ROOK_1 = Piece("Rook", "Black", "r", 7, 0, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_rook.png")), (self.WIDTH, self.HEIGHT)), -5, self)
        self.BLACK_KNIGHT_1 = Piece("Knight", "Black", "n", 7, 1, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_knight.png")), (self.WIDTH, self.HEIGHT)), -3.5, self)
        self.BLACK_BISHOP_1 = Piece("Bishop", "Black", "b", 7, 2, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_bishop.png")), (self.WIDTH, self.HEIGHT)), -3, self)
        self.BLACK_QUEEN = Piece("Queen", "Black", "q", 7, 3, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_queen.png")), (self.WIDTH, self.HEIGHT)), -9, self)
        self.BLACK_KING = Piece("King", "Black", "k", 7, 4, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_king.png")), (self.WIDTH, self.HEIGHT)), -100, self)
        self.BLACK_BISHOP_2 = Piece("Bishop", "Black", "b", 7, 5, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_bishop.png")), (self.WIDTH, self.HEIGHT)), -3.5, self)
        self.BLACK_KNIGHT_2 = Piece("Knight", "Black", "n", 7, 6, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_knight.png")), (self.WIDTH, self.HEIGHT)), -3, self)
        self.BLACK_ROOK_2 = Piece("Rook", "Black", "r", 7, 7, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_rook.png")), (self.WIDTH, self.HEIGHT)), -5, self)
        self.BLACK_PAWN_1 = Piece("Pawn", "Black", "p", 6, 0, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_pawn.png")), (self.WIDTH, self.HEIGHT)), -1, self)
        self.BLACK_PAWN_2 = Piece("Pawn", "Black", "p", 6, 1, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_pawn.png")), (self.WIDTH, self.HEIGHT)), -1, self)
        self.BLACK_PAWN_3 = Piece("Pawn", "Black", "p", 6, 2, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_pawn.png")), (self.WIDTH, self.HEIGHT)), -1, self)
        self.BLACK_PAWN_4 = Piece("Pawn", "Black", "p", 6, 3, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_pawn.png")), (self.WIDTH, self.HEIGHT)), -1, self)
        self.BLACK_PAWN_5 = Piece("Pawn", "Black", "p", 6, 4, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_pawn.png")), (self.WIDTH, self.HEIGHT)), -1, self)
        self.BLACK_PAWN_6 = Piece("Pawn", "Black", "p", 6, 5, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_pawn.png")), (self.WIDTH, self.HEIGHT)), -1, self)
        self.BLACK_PAWN_7 = Piece("Pawn", "Black", "p", 6, 6, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_pawn.png")), (self.WIDTH, self.HEIGHT)), -1, self)
        self.BLACK_PAWN_8 = Piece("Pawn", "Black", "p", 6, 7, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_pawn.png")), (self.WIDTH, self.HEIGHT)), -1, self)
        self.EMPTY = Piece("Empty", None, " ", None, None, None, 0, self)
        self.LIGHT_SQUARE = (255, 206, 158)
        self.DARK_SQUARE = (209, 139, 71)
        self.SQUARE_SIZE = 100
        self.piece_board = [
            [self.WHITE_ROOK_1, self.WHITE_KNIGHT_1, self.WHITE_BISHOP_1, self.WHITE_KING,
                self.WHITE_QUEEN,  self.WHITE_BISHOP_2, self.WHITE_KNIGHT_2, self.WHITE_ROOK_2],
            [self.WHITE_PAWN_1, self.WHITE_PAWN_2, self.WHITE_PAWN_3, self.WHITE_PAWN_4,
                self.WHITE_PAWN_5, self.WHITE_PAWN_6, self.WHITE_PAWN_7, self.WHITE_PAWN_8],
            [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY,
                self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY,
                self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY,
                self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY,
                self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
            [self.BLACK_PAWN_1, self.BLACK_PAWN_2, self.BLACK_PAWN_3, self.BLACK_PAWN_4,
                self.BLACK_PAWN_5, self.BLACK_PAWN_6, self.BLACK_PAWN_7, self.BLACK_PAWN_8],
            [self.BLACK_ROOK_1, self.BLACK_KNIGHT_1, self.BLACK_BISHOP_1, self.BLACK_KING,
                self.BLACK_QUEEN, self.BLACK_BISHOP_2, self.BLACK_KNIGHT_2, self.BLACK_ROOK_2]
        ]
        self.bg_board = [
            ["L", "D", "L", "D", "L", "D", "L", "D"],
            ["D", "L", "D", "L", "D", "L", "D", "L"],
            ["L", "D", "L", "D", "L", "D", "L", "D"],
            ["D", "L", "D", "L", "D", "L", "D", "L"],
            ["L", "D", "L", "D", "L", "D", "L", "D"],
            ["D", "L", "D", "L", "D", "L", "D", "L"],
            ["L", "D", "L", "D", "L", "D", "L", "D"],
            ["D", "L", "D", "L", "D", "L", "D", "L"]
        ]
        self.board_states = [self.piece_board]
        self.white_to_move = True
        self.cant_move = False

    def update_board(self, new_board):
        self.bg_board = new_board

    def draw(self, WIN):
        for row in range(8):
            for col in range(8):
                rect = p.Rect(row*self.SQUARE_SIZE, col*self.SQUARE_SIZE,
                              self.SQUARE_SIZE, self.SQUARE_SIZE)
                if self.bg_board[row][col] == "D":
                    p.draw.rect(WIN, self.DARK_SQUARE, rect)
                else:
                    p.draw.rect(WIN, self.LIGHT_SQUARE, rect)
        for row in range(8):
            for col in range(8):
                if self.piece_board[row][col].type != "Empty":
                    self.piece_board[row][col].draw(WIN)

    def add_state(self, new_state):
        self.board_states.append(new_state)

    def previous_state(self):
        if (self.board_states.index(self.piece_board) > 0):
            temp = self.board_states[self.board_states.index(
                self.piece_board)-1]
            self.piece_board = temp
            self.cant_move = True

    def next_state(self):
        if self.board_states.index(self.piece_board) < len(self.board_states)-1:
            temp = self.board_states[self.board_states.index(
                self.piece_board)+1]
            self.piece_board = temp
            self.cant_move = True
        if self.board_states.index(self.piece_board) == len(self.board_states)-1:
            self.cant_move = False

    def king_in_check(self, other_board):
        if (other_board == None):
            if self.white_to_move:
                next_legal_moves = self.get_psuedo_legal_moves()
                if (self.WHITE_KING.location in next_legal_moves):
                    self.cant_move = True
                    return True
            else:
                next_legal_moves = self.get_psuedo_legal_moves()
                if (self.BLACK_KING.location in next_legal_moves):
                    self.cant_move = True
                    return True
        else:
            if self.white_to_move:
                next_legal_moves = other_board.get_psuedo_legal_moves()
                if (self.WHITE_KING.location in next_legal_moves):
                    self.cant_move = True
                    return True
            else:
                next_legal_moves = other_board.get_psuedo_legal_moves()
                if (self.BLACK_KING.location in next_legal_moves):
                    self.cant_move = True
                    return True
        return False

    def get_uncheck_moves(self):
        fake_board = Board(100, 100)
        fake_board.piece_board = self.piece_board
        legal_moves = []
        if self.white_to_move:
            for row in fake_board.piece_board:
                for piece in row:
                    if piece.color == "White":
                        for move in piece.get_psuedo_legal_moves():
                            piece.move_to(move[0], move[1])
                            if (not fake_board.king_in_check(fake_board)):
                                legal_moves.append(move)
                        fake_board.piece_board = self.piece_board
        else:
            for row in fake_board.piece_board:
                for piece in row:
                    if piece.color == "Black":
                        for move in piece.get_psuedo_legal_moves():
                            piece.move_to(move[0], move[1])
                            if (not fake_board.king_in_check(fake_board)):
                                legal_moves.append(move)
                        fake_board.piece_board = self.piece_board
        return legal_moves

    def get_piece(self, row, col):
        return self.piece_board[row][col]

    def get_legal_moves(self):
        legal_moves = []
        for row in self.piece_board:
            for piece in row:
                if self.white_to_move == (piece.color == "White"):
                    legal_moves += (piece.location,
                                    piece.get_legal_moves())
        return legal_moves

    def make_move(self, move):
        self.piece_board[move[0][0]][move[0][1]].move_to(
            move[1][0], move[1][1], self, self.white_to_move)
        self.white_to_move = not self.white_to_move
        self.add_state(self.piece_board)
    def get_psuedo_legal_moves(self):
        legal_moves = []
        for row in self.piece_board:
            for piece in row:
                if self.white_to_move == (piece.color == "White"):
                    legal_moves += (piece.location,
                                    piece.get_psuedo_legal_moves())
        return legal_moves
