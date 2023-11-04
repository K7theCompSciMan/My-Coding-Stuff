import time
import pygame as p


class Piece:

    def __init__(self, type, color, symbol, rank, file, image, value, board) -> None:
        self.type = type
        self.color = color
        self.symbol = symbol
        self.rank = rank
        self.file = file
        self.location = (rank, file)
        self.original_location = (rank, file)
        self.image = image
        self.value = value
        if (self.image != None):
            self.rect = p.Rect(self.file*100, self.rank*100, 100, 100)
        self.board = board

    def __str__(self) -> str:
        return self.symbol

    def move_to(self, rank, file):
        if ((rank, file) in self.get_psuedo_legal_moves() and self.board.white_to_move == (self.color == "White")):

            self.board.piece_board[self.rank][self.file] = self.board.EMPTY
            self.rank = rank
            self.file = file
            self.location = (rank, file)
            self.board.piece_board[self.rank][self.file] = self.board.EMPTY
            self.board.piece_board[self.rank][self.file] = self
            self.rect = p.Rect(self.file*100, self.rank*100, 100, 100)
            self.board.white_to_move = not self.board.white_to_move

    def get_legal_moves(self: list):
        legal_moves = []
        match self.type:
            case  "Pawn":
                legal_moves = self.get_pawn_moves()
            case "King":
                legal_moves = self.get_king_moves()
            case "Rook":
                legal_moves = self.get_rook_moves()
            case "Knight":
                legal_moves = self.get_knight_moves()
            case "Bishop":
                legal_moves = self.get_bishop_moves()
            case "Queen":
                legal_moves = self.get_queen_moves()
        if(self.board.king_in_check(None)):
            for move in legal_moves:
                if move in self.board.get_uncheck_moves():
                    pass
                else:
                    legal_moves.remove(move)
        
        return legal_moves

    def get_queen_moves(self):
        legal_moves = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for direction in directions:
            target_rank = self.rank + direction[0]
            target_file = self.file + direction[1]

            while 0 <= target_rank <= 7 and 0 <= target_file <= 7:
                target_square = self.board.piece_board[target_rank][target_file]

                if target_square.color is None:
                    legal_moves.append((target_rank, target_file))
                elif target_square.color != self.color:
                    legal_moves.append((target_rank, target_file))
                    break
                else:
                    break

                target_rank += direction[0]
                target_file += direction[1]
        counts = [0, 0, 0, 0]
        for i in range(1, 9):
            directions = [(i, i), (-i, -i), (i, -i), (-i, i)]
            for i in range(0, 4):
                    try: 
                        target_square = (self.rank + directions[i][0], self.file + directions[i][1])
                        if (0 <= target_square[0] <= 7 and 0 <= target_square[1] <= 7 and self.board.piece_board[target_square[0]][target_square[1]].color != self.color and counts[i] == 0 and (not target_square in legal_moves)):
                            legal_moves.append(target_square)
                        if (self.board.piece_board[target_square[0]][target_square[1]].color != None):
                            counts[i] = 1
                    except:
                        pass
        return legal_moves

    def get_pawn_moves(self):
        legal_moves = []
        if (self.color == "White"):
            if (self.rank == 1 and self.board.piece_board[self.rank + 1][self.file].color == None):
                legal_moves.append((self.rank + 1, self.file))
                legal_moves.append((self.rank + 2, self.file))
            elif (self.rank + 1 < 8 and self.board.piece_board[self.rank + 1][self.file].color == None):
                legal_moves.append((self.rank + 1, self.file))
            if (self.file + 1 < 8 and self.rank + 1 < 8):
                target_square = self.board.piece_board[self.rank + 1][self.file + 1]
                if (target_square.color == "Black"):
                    legal_moves.append((self.rank + 1, self.file + 1))
            if (self.file-1 >= 0 and self.rank + 1 < 8):
                target_square = self.board.piece_board[self.rank + 1][self.file - 1]
                if (target_square.color == "Black"):
                    legal_moves.append((self.rank + 1, self.file - 1))
        else:
            if (self.rank == 6 and self.board.piece_board[self.rank - 1][self.file].color == None):
                legal_moves.append((self.rank - 1, self.file))
                legal_moves.append((self.rank - 2, self.file))
            elif (self.rank-1 >= 0 and self.board.piece_board[self.rank - 1][self.file].color == None):
                legal_moves.append((self.rank - 1, self.file))
            if (self.file + 1 < 8 and self.rank - 1 >= 0):
                target_square = self.board.piece_board[self.rank - 1][self.file + 1]
                if (target_square.color == "White"):
                    legal_moves.append((self.rank - 1, self.file + 1))
            if (self.file-1 >= 0 and self.rank - 1 >= 0):
                target_square = self.board.piece_board[self.rank - 1][self.file - 1]
                if (target_square.color == "White"):
                    legal_moves.append((self.rank - 1, self.file - 1))
        return legal_moves

    def get_king_moves(self):
        legal_moves = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for direction in directions:
            target_rank = self.rank + direction[0]
            target_file = self.file + direction[1]

            if 0 <= target_rank <= 7 and 0 <= target_file <= 7:
                target_square = self.board.piece_board[target_rank][target_file]

                if target_square.color != self.color:
                    legal_moves.append((target_rank, target_file))

        return legal_moves

    def get_rook_moves(self):
        legal_moves = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for direction in directions:
            target_rank = self.rank + direction[0]
            target_file = self.file + direction[1]

            while 0 <= target_rank <= 7 and 0 <= target_file <= 7:
                target_square = self.board.piece_board[target_rank][target_file]

                if target_square.color is None:
                    legal_moves.append((target_rank, target_file))
                elif target_square.color != self.color:
                    legal_moves.append((target_rank, target_file))
                    break
                else:
                    break

                target_rank += direction[0]
                target_file += direction[1]

        return legal_moves

    def get_knight_moves(self):
        legal_moves = []
        if (self.file + 2 < 8 and self.rank + 1 < 8):
            target_square = self.board.piece_board[self.rank + 1][self.file + 2]
            if (target_square.color != self.color):
                legal_moves.append((self.rank + 1, self.file + 2))
        if (self.file + 2 < 8 and self.rank - 1 >= 0):
            target_square = self.board.piece_board[self.rank - 1][self.file + 2]
            if (target_square.color != self.color):
                legal_moves.append((self.rank - 1, self.file + 2))
        if (self.file - 2 >= 0 and self.rank + 1 < 8):
            target_square = self.board.piece_board[self.rank + 1][self.file - 2]
            if (target_square.color != self.color):
                legal_moves.append((self.rank + 1, self.file - 2))
        if (self.file - 2 >= 0 and self.rank - 1 >= 0):
            target_square = self.board.piece_board[self.rank - 1][self.file - 2]
            if (target_square.color != self.color):
                legal_moves.append((self.rank - 1, self.file - 2))
        if (self.file + 1 < 8 and self.rank + 2 < 8):
            target_square = self.board.piece_board[self.rank + 2][self.file + 1]
            if (target_square.color != self.color):
                legal_moves.append((self.rank + 2, self.file + 1))
        if (self.file + 1 < 8 and self.rank - 2 >= 0):
            target_square = self.board.piece_board[self.rank - 2][self.file + 1]
            if (target_square.color != self.color):
                legal_moves.append((self.rank - 2, self.file + 1))
        if (self.file - 1 >= 0 and self.rank + 2 < 8):
            target_square = self.board.piece_board[self.rank + 2][self.file - 1]
            if (target_square.color != self.color):
                legal_moves.append((self.rank + 2, self.file - 1))
        if (self.file - 1 >= 0 and self.rank - 2 >= 0):
            target_square = self.board.piece_board[self.rank - 2][self.file - 1]
            # if(target_square.color != self.color):
            legal_moves.append((self.rank - 2, self.file - 1))
        return legal_moves

    def get_bishop_moves(self):
        legal_moves = []
        counts = [0, 0, 0, 0]
        for i in range(1, 9):
            directions = [(i, i), (-i, -i), (i, -i), (-i, i)]
            for i in range(0, 4):
                    try: 
                        target_square = (self.rank + directions[i][0], self.file + directions[i][1])
                        if (0 <= target_square[0] <= 7 and 0 <= target_square[1] <= 7 and self.board.piece_board[target_square[0]][target_square[1]].color != self.color and counts[i] == 0 and (not target_square in legal_moves)):
                            legal_moves.append(target_square)
                        if (self.board.piece_board[target_square[0]][target_square[1]].color != None):
                            counts[i] = 1
                    except:
                        pass
        return legal_moves


    def is_clicked(self, event):
        if event.type == p.MOUSEBUTTONDOWN:
            if (self.rect.collidepoint(event.pos)):
                return True

    def draw(self, WIN):
        WIN.blit(self.image, self.rect)

    def display_legal_moves(self, WIN: p.Surface):
        legal_moves = self.get_legal_moves()
        for move in legal_moves:
            p.draw.circle(WIN, (0, 255, 0),
                          ((move[1]*100 + 50), (move[0]*100 + 50)), 10)

    def is_legal_move(self, rank, file):
        if ((rank, file) in self.get_legal_moves()):
            return True
    def get_value(self):
        return self.value
    def get_psuedo_legal_moves(self):
        legal_moves = []
        match self.type:
            case  "Pawn":
                legal_moves = self.get_pawn_moves()
            case "King":
                legal_moves = self.get_king_moves()
            case "Rook":
                legal_moves = self.get_rook_moves()
            case "Knight":
                legal_moves = self.get_knight_moves()
            case "Bishop":
                legal_moves = self.get_bishop_moves()
            case "Queen":
                legal_moves = self.get_queen_moves()
        return legal_moves