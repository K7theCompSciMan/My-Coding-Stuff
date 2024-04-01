import os
import pygame as p
from Piece import Piece


class Board:
    def __init__(self, image_width, image_height) -> None:
        self.WIDTH = image_width
        self.HEIGHT = image_height
        self.WHITE_ROOK_1 = Piece("Rook", "White", "R", 0, 0, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_rook.png")), (self.WIDTH, self.HEIGHT)))
        self.WHITE_KNIGHT_1 = Piece("Knight", "White", "N", 0, 1, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_knight.png")), (self.WIDTH, self.HEIGHT)))
        self.WHITE_BISHOP_1 = Piece("Bishop", "White", "B", 0, 2, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_bishop.png")), (self.WIDTH, self.HEIGHT)))
        self.WHITE_QUEEN = Piece("Queen", "White", "Q", 0, 3, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_queen.png")), (self.WIDTH, self.HEIGHT)))
        self.WHITE_KING = Piece("King", "White", "K", 0, 4, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_king.png")), (self.WIDTH, self.HEIGHT)))
        self.WHITE_BISHOP_2 = Piece("Bishop", "White", "B", 0, 5, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_bishop.png")), (self.WIDTH, self.HEIGHT)))
        self.WHITE_KNIGHT_2 = Piece("Knight", "White", "N", 0, 6, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_knight.png")), (self.WIDTH, self.HEIGHT)))
        self.WHITE_ROOK_2 = Piece("Rook", "White", "R", 0, 7, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_rook.png")), (self.WIDTH, self.HEIGHT)))
        self.WHITE_PAWN_1 = Piece("Pawn", "White", "P", 1, 0, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_pawn.png")), (self.WIDTH, self.HEIGHT)))
        self.WHITE_PAWN_2 = Piece("Pawn", "White", "P", 1, 1, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_pawn.png")), (self.WIDTH, self.HEIGHT)))
        self.WHITE_PAWN_3 = Piece("Pawn", "White", "P", 1, 2, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_pawn.png")), (self.WIDTH, self.HEIGHT)))
        self.WHITE_PAWN_4 = Piece("Pawn", "White", "P", 1, 3, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_pawn.png")), (self.WIDTH, self.HEIGHT)))
        self.WHITE_PAWN_5 = Piece("Pawn", "White", "P", 1, 4, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_pawn.png")), (self.WIDTH, self.HEIGHT)))
        self.WHITE_PAWN_6 = Piece("Pawn", "White", "P", 1, 5, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_pawn.png")), (self.WIDTH, self.HEIGHT)))
        self.WHITE_PAWN_7 = Piece("Pawn", "White", "P", 1, 6, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_pawn.png")), (self.WIDTH, self.HEIGHT)))
        self.WHITE_PAWN_8 = Piece("Pawn", "White", "P", 1, 7, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "white_pawn.png")), (self.WIDTH, self.HEIGHT)))

        self.BLACK_ROOK_1 = Piece("Rook", "Black", "r", 7, 0, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_rook.png")), (self.WIDTH, self.HEIGHT)))
        self.BLACK_KNIGHT_1 = Piece("Knight", "Black", "n", 7, 1, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_knight.png")), (self.WIDTH, self.HEIGHT)))
        self.BLACK_BISHOP_1 = Piece("Bishop", "Black", "b", 7, 2, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_bishop.png")), (self.WIDTH, self.HEIGHT)))
        self.BLACK_QUEEN = Piece("Queen", "Black", "q", 7, 3, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_queen.png")), (self.WIDTH, self.HEIGHT)))
        self.BLACK_KING = Piece("King", "Black", "k", 7, 4, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_king.png")), (self.WIDTH, self.HEIGHT)))
        self.BLACK_BISHOP_2 = Piece("Bishop", "Black", "b", 7, 5, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_bishop.png")), (self.WIDTH, self.HEIGHT)))
        self.BLACK_KNIGHT_2 = Piece("Knight", "Black", "n", 7, 6, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_knight.png")), (self.WIDTH, self.HEIGHT)))
        self.BLACK_ROOK_2 = Piece("Rook", "Black", "r", 7, 7, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_rook.png")), (self.WIDTH, self.HEIGHT)))
        self.BLACK_PAWN_1 = Piece("Pawn", "Black", "p", 6, 0, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_pawn.png")), (self.WIDTH, self.HEIGHT)))
        self.BLACK_PAWN_2 = Piece("Pawn", "Black", "p", 6, 1, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_pawn.png")), (self.WIDTH, self.HEIGHT)))
        self.BLACK_PAWN_3 = Piece("Pawn", "Black", "p", 6, 2, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_pawn.png")), (self.WIDTH, self.HEIGHT)))
        self.BLACK_PAWN_4 = Piece("Pawn", "Black", "p", 6, 3, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_pawn.png")), (self.WIDTH, self.HEIGHT)))
        self.BLACK_PAWN_5 = Piece("Pawn", "Black", "p", 6, 4, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_pawn.png")), (self.WIDTH, self.HEIGHT)))
        self.BLACK_PAWN_6 = Piece("Pawn", "Black", "p", 6, 5, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_pawn.png")), (self.WIDTH, self.HEIGHT)))
        self.BLACK_PAWN_7 = Piece("Pawn", "Black", "p", 6, 6, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_pawn.png")), (self.WIDTH, self.HEIGHT)))
        self.BLACK_PAWN_8 = Piece("Pawn", "Black", "p", 6, 7, p.transform.scale(p.image.load(os.path.join(
            'Python', 'Neural Networks and AI stuff', "Chess AI", "images", "black_pawn.png")), (self.WIDTH, self.HEIGHT)))
        self.EMPTY = Piece("Empty", None, "", None, None, None)
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
        if(self.board_states.index(self.piece_board) > 0):
            temp = self.board_states[self.board_states.index(self.piece_board)-1]
            self.piece_board = temp
            self.cant_move = True
    def next_state(self):
        if self.board_states.index(self.piece_board) < len(self.board_states)-1:
            temp = self.board_states[self.board_states.index(self.piece_board)+1]
            self.piece_board = temp
            self.cant_move = True
        if self.board_states.index(self.piece_board) == len(self.board_states)-1:
            self.cant_move = False
