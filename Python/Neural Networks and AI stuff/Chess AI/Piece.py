import time
import pygame as p


class Piece:

    def __init__(self, type, color, symbol, rank, file, image) -> None:
        self.type = type
        self.color = color
        self.symbol = symbol
        self.rank = rank
        self.file = file
        self.location = (rank, file)
        self.original_location = (rank, file)
        self.image = image
        if (self.image != None):
            self.rect = p.Rect(self.file*100, self.rank*100, 100, 100)

    def __str__(self) -> str:
        return self.symbol

    def move_to(self, rank, file, board, white_to_move):
        if ((rank, file) in self.get_legal_moves(board.piece_board) and white_to_move == (self.color == "White")):

            board.piece_board[self.rank][self.file] = board.EMPTY
            self.rank = rank
            self.file = file
            self.location = (rank, file)
            board.piece_board[self.rank][self.file] = board.EMPTY
            board.piece_board[self.rank][self.file] = self
            self.rect = p.Rect(self.file*100, self.rank*100, 100, 100)

    def get_legal_moves(self, board: list):
        legal_moves = []
        match self.type:
            case  "Pawn":
                legal_moves = self.get_pawn_moves(board)
            case "King":
                legal_moves = self.get_king_moves(board)
            case "Rook":
                legal_moves = self.get_rook_moves(board)
            case "Knight":
                legal_moves = self.get_knight_moves(board)
            case "Bishop":
                legal_moves = self.get_bishop_moves(board)
            case "Queen":
                legal_moves = self.get_queen_moves(board)
        return legal_moves

    def get_queen_moves(self, board):
        legal_moves = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for direction in directions:
            target_rank = self.rank + direction[0]
            target_file = self.file + direction[1]

            while 0 <= target_rank <= 7 and 0 <= target_file <= 7:
                target_square = board[target_rank][target_file]

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
                        if (0 <= target_square[0] <= 7 and 0 <= target_square[1] <= 7 and board[target_square[0]][target_square[1]].color != self.color and counts[i] == 0 and (not target_square in legal_moves)):
                            legal_moves.append(target_square)
                        if (board[target_square[0]][target_square[1]].color != None):
                            counts[i] = 1
                    except:
                        pass
        return legal_moves

    def get_pawn_moves(self, board):
        legal_moves = []
        if (self.color == "White"):
            if (self.rank == 1 and board[self.rank + 1][self.file].color == None):
                legal_moves.append((self.rank + 1, self.file))
                legal_moves.append((self.rank + 2, self.file))
            elif (self.rank + 1 < 8 and board[self.rank + 1][self.file].color == None):
                legal_moves.append((self.rank + 1, self.file))
            if (self.file + 1 < 8 and self.rank + 1 < 8):
                target_square = board[self.rank + 1][self.file + 1]
                if (target_square.color == "Black"):
                    legal_moves.append((self.rank + 1, self.file + 1))
            if (self.file-1 >= 0 and self.rank + 1 < 8):
                target_square = board[self.rank + 1][self.file - 1]
                if (target_square.color == "Black"):
                    legal_moves.append((self.rank + 1, self.file - 1))
        else:
            if (self.rank == 6 and board[self.rank - 1][self.file].color == None):
                legal_moves.append((self.rank - 1, self.file))
                legal_moves.append((self.rank - 2, self.file))
            elif (self.rank-1 >= 0 and board[self.rank - 1][self.file].color == None):
                legal_moves.append((self.rank - 1, self.file))
            if (self.file + 1 < 8 and self.rank - 1 >= 0):
                target_square = board[self.rank - 1][self.file + 1]
                if (target_square.color == "White"):
                    legal_moves.append((self.rank - 1, self.file + 1))
            if (self.file-1 >= 0 and self.rank - 1 >= 0):
                target_square = board[self.rank - 1][self.file - 1]
                if (target_square.color == "White"):
                    legal_moves.append((self.rank - 1, self.file - 1))
        return legal_moves

    def get_king_moves(self, board):
        legal_moves = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for direction in directions:
            target_rank = self.rank + direction[0]
            target_file = self.file + direction[1]

            if 0 <= target_rank <= 7 and 0 <= target_file <= 7:
                target_square = board[target_rank][target_file]

                if target_square.color != self.color:
                    legal_moves.append((target_rank, target_file))

        return legal_moves

    def get_rook_moves(self, board):
        legal_moves = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for direction in directions:
            target_rank = self.rank + direction[0]
            target_file = self.file + direction[1]

            while 0 <= target_rank <= 7 and 0 <= target_file <= 7:
                target_square = board[target_rank][target_file]

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

    def get_knight_moves(self, board):
        legal_moves = []
        if (self.file + 2 < 8 and self.rank + 1 < 8):
            target_square = board[self.rank + 1][self.file + 2]
            if (target_square.color != self.color):
                legal_moves.append((self.rank + 1, self.file + 2))
        if (self.file + 2 < 8 and self.rank - 1 >= 0):
            target_square = board[self.rank - 1][self.file + 2]
            if (target_square.color != self.color):
                legal_moves.append((self.rank - 1, self.file + 2))
        if (self.file - 2 >= 0 and self.rank + 1 < 8):
            target_square = board[self.rank + 1][self.file - 2]
            if (target_square.color != self.color):
                legal_moves.append((self.rank + 1, self.file - 2))
        if (self.file - 2 >= 0 and self.rank - 1 >= 0):
            target_square = board[self.rank - 1][self.file - 2]
            if (target_square.color != self.color):
                legal_moves.append((self.rank - 1, self.file - 2))
        if (self.file + 1 < 8 and self.rank + 2 < 8):
            target_square = board[self.rank + 2][self.file + 1]
            if (target_square.color != self.color):
                legal_moves.append((self.rank + 2, self.file + 1))
        if (self.file + 1 < 8 and self.rank - 2 >= 0):
            target_square = board[self.rank - 2][self.file + 1]
            if (target_square.color != self.color):
                legal_moves.append((self.rank - 2, self.file + 1))
        if (self.file - 1 >= 0 and self.rank + 2 < 8):
            target_square = board[self.rank + 2][self.file - 1]
            if (target_square.color != self.color):
                legal_moves.append((self.rank + 2, self.file - 1))
        if (self.file - 1 >= 0 and self.rank - 2 >= 0):
            target_square = board[self.rank - 2][self.file - 1]
            # if(target_square.color != self.color):
            legal_moves.append((self.rank - 2, self.file - 1))
        return legal_moves

    def get_bishop_moves(self, board):
        legal_moves = []
        counts = [0, 0, 0, 0]
        for i in range(1, 9):
            directions = [(i, i), (-i, -i), (i, -i), (-i, i)]
            for i in range(0, 4):
                    try: 
                        target_square = (self.rank + directions[i][0], self.file + directions[i][1])
                        if (0 <= target_square[0] <= 7 and 0 <= target_square[1] <= 7 and board[target_square[0]][target_square[1]].color != self.color and counts[i] == 0 and (not target_square in legal_moves)):
                            legal_moves.append(target_square)
                        if (board[target_square[0]][target_square[1]].color != None):
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

    def display_legal_moves(self, board, WIN: p.Surface):
        legal_moves = self.get_legal_moves(board.piece_board)
        for move in legal_moves:
            p.draw.circle(WIN, (0, 255, 0),
                          ((move[1]*100 + 50), (move[0]*100 + 50)), 10)

    def is_legal_move(self, rank, file, board):
        if ((rank, file) in self.get_legal_moves(board.piece_board)):
            return True
