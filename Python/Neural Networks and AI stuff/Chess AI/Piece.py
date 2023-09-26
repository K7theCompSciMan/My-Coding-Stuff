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
                self.image = image

                
        def __str__(self) -> str:
                return self.symbol
        def move_to(self, rank, file, board):
                board.piece_board[self.rank][self.file] = board.EMPTY
                self.rank = rank
                self.file = file
                self.location = (rank, file)
                board.piece_board[self.rank][self.file] = self
        def get_legal_moves(self, board):
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
                                legal_moves.append(self.get_rook_moves(board) + self.get_bishop_moves(board))
                return legal_moves
        
        
        def get_pawn_moves(self, board):
                legal_moves = []
                if(self.color == "White"):
                        if(self.rank == 1 and board[self.rank + 1][self.file].color == None):
                                legal_moves.append((self.rank + 1, self.file))
                                legal_moves.append((self.rank + 2, self.file))
                        elif(self.rank +1 < 8 and board[self.rank + 1][self.file].color == None):
                                legal_moves.append((self.rank + 1, self.file))
                        if(self.file + 1 < 8 and self.rank + 1 < 8):
                                target_square = board[self.rank + 1][self.file + 1]
                                if(target_square.color == "Black"):
                                        legal_moves.append((self.rank + 1, self.file + 1))
                        if(self.file-1 >= 0 and self.rank + 1 < 8):
                                target_square = board[self.rank + 1][self.file - 1]
                                if(target_square.color == "Black"):
                                        legal_moves.append((self.rank + 1, self.file - 1))
                else:
                        if(self.rank == 6 and board[self.rank - 1][self.file].color == None):
                                legal_moves.append((self.rank - 1, self.file))
                                legal_moves.append((self.rank - 2, self.file))
                        elif(self.rank-1 >=0 and board[self.rank - 1][self.file].color == None):
                                legal_moves.append((self.rank - 1, self.file))
                        if(self.file + 1 < 8 and self.rank -1 >= 0):
                                target_square = board[self.rank - 1][self.file + 1]
                                if(target_square.color == "White"):
                                        legal_moves.append((self.rank - 1, self.file + 1))
                        if(self.file-1 >= 0 and self.rank -1 >= 0):
                                target_square = board[self.rank - 1][self.file - 1]
                                if(target_square.color == "White"):
                                        legal_moves.append((self.rank - 1, self.file - 1))
                return legal_moves

        def get_king_moves(self, board):
                legal_moves = []
                if(self.file + 1 < 8):
                        target_square = board[self.rank][self.file + 1]
                        if(target_square.color != self.color):
                                legal_moves.append((self.rank, self.file + 1))
                if(self.file - 1 >= 0):
                        target_square = board[self.rank][self.file - 1]
                        if(target_square.color != self.color):
                                legal_moves.append((self.rank, self.file - 1))
                if(self.rank + 1 < 8):
                        target_square = board[self.rank + 1][self.file]
                        if(target_square.color != self.color):
                                legal_moves.append((self.rank + 1, self.file))
                if(self.rank - 1 >= 0):
                        target_square = board[self.rank - 1][self.file]
                        if(target_square.color != self.color):
                                legal_moves.append((self.rank - 1, self.file))
                if(self.file + 1 < 8 and self.rank + 1 < 8):
                        target_square = board[self.rank + 1][self.file + 1]
                        if(target_square.color != self.color):
                                legal_moves.append((self.rank + 1, self.file + 1))
                if(self.file + 1 < 8 and self.rank - 1 >= 0):
                        target_square = board[self.rank - 1][self.file + 1]
                        if(target_square.color != self.color):
                                legal_moves.append((self.rank - 1, self.file + 1))
                if(self.file - 1 >= 0 and self.rank + 1 < 8):
                        target_square = board[self.rank + 1][self.file - 1]
                        if(target_square.color != self.color):
                                legal_moves.append((self.rank + 1, self.file - 1))
                return legal_moves

        def get_rook_moves(self, board):
                legal_moves = []
                count_1 = 0
                count_2 = 0
                count_3 = 0
                count_4 = 0
                for i in range(7, -1, -1):
                        try:
                                if(self.rank - i >= 0):
                                        target_square_3 = board[self.rank - i][self.file]
                                        if(target_square_3.color != self.color and count_3 < 1):
                                                if (target_square_3.color != None):
                                                        count_3 += 1
                                                target_location = (self.rank - i, self.file)
                                                if (not (target_location in legal_moves) ):
                                                        legal_moves.append(target_location)
                        except:
                                pass
                for i in range(1, 8):
                        try:
                                target_square_1 = board[self.rank + i][self.file]
                                if(target_square_1.color != self.color and count_1 < 1):
                                        if (target_square_1.color != None):
                                                count_1 += 1
                                        target_location = (self.rank + i, self.file)
                                        if (not (target_location in legal_moves) ):
                                                legal_moves.append(target_location)
                        except:
                                pass
                        
                for i in range(1, 8):
                        try:
                                if(self.file - i >= 0):
                                        target_square_4 = board[self.rank][self.file - i]
                                        if(target_square_4.color != self.color and count_4 < 1):
                                                if (target_square_4.color != None):
                                                        count_4 += 1
                                                target_location = (self.rank, self.file - i)
                                                if (not (target_location in legal_moves) ):
                                                        legal_moves.append(target_location)
                        except:
                                pass
                for i in range(1, 8):
                        try:
                                target_square_2 = board[self.rank][self.file + i]
                                if(target_square_2.color != self.color and count_2 < 1):
                                        if (target_square_2.color != None):
                                                count_2 += 1
                                        target_location = (self.rank, self.file + i)
                                        if (not (target_location in legal_moves) ):
                                                legal_moves.append(target_location)
                        except:
                                pass
                legal_moves.remove((self.rank, self.file))
                return legal_moves
        
        def get_knight_moves(self, board):
                legal_moves = []
                if(self.file + 2 < 8 and self.rank + 1 < 8):
                        target_square = board[self.rank + 1][self.file + 2]
                        if(target_square.color != self.color):
                                legal_moves.append((self.rank + 1, self.file + 2))
                if(self.file + 2 < 8 and self.rank - 1 >= 0):
                        target_square = board[self.rank - 1][self.file + 2]
                        if(target_square.color != self.color):
                                legal_moves.append((self.rank - 1, self.file + 2))
                if(self.file - 2 >= 0 and self.rank + 1 < 8):
                        target_square = board[self.rank + 1][self.file - 2]
                        if(target_square.color != self.color):
                                legal_moves.append((self.rank + 1, self.file - 2))
                if(self.file - 2 >= 0 and self.rank - 1 >= 0):
                        target_square = board[self.rank - 1][self.file - 2]
                        if(target_square.color != self.color):
                                legal_moves.append((self.rank - 1, self.file - 2))
                if(self.file + 1 < 8 and self.rank + 2 < 8):
                        target_square = board[self.rank + 2][self.file + 1]
                        if(target_square.color != self.color):
                                legal_moves.append((self.rank + 2, self.file + 1))
                if(self.file + 1 < 8 and self.rank - 2 >= 0):
                        target_square = board[self.rank - 2][self.file + 1]
                        if(target_square.color != self.color):
                                legal_moves.append((self.rank - 2, self.file + 1))
                if(self.file - 1 >= 0 and self.rank + 2 < 8):
                        target_square = board[self.rank + 2][self.file - 1]
                        if(target_square.color != self.color):
                                legal_moves.append((self.rank + 2, self.file - 1))
                if(self.file - 1 >= 0 and self.rank - 2 >= 0):
                        target_square = board[self.rank - 2][self.file - 1]
                        if(target_square.color != self.color):
                                legal_moves.append((self.rank - 2, self.file - 1))
                return legal_moves

        def get_bishop_moves(self, board):
                legal_moves = []
                count_1 = 0
                count_2 = 0
                count_3 = 0;
                count_4 = 0;
                
                for i in range(1, 9):
                                try:
                                        
                                        target_square_1 = board[self.rank + i][self.file + i]
                                        if(target_square_1.color != self.color and count_1 < 1):
                                                if target_square_1.color != None:
                                                        count_1+=1
                                                target_location = (self.rank + i, self.file + i)
                                                if (not (target_location in legal_moves) ):
                                                        legal_moves.append(target_location)
                                except:
                                        pass
                                try:
                                        if(self.file - i >= 0 and self.rank - i >= 0):
                                                target_square_2 = board[self.rank - i][self.file - i]
                                                if(target_square_2.color != self.color and count_2 < 1):
                                                        if target_square_2.color != None:
                                                                count_2+=1
                                                        target_location = (self.rank - i, self.file - i)
                                                        if (not (target_location in legal_moves)  ):
                                                                legal_moves.append(target_location)
                                except:
                                        pass

                                try:
                                        if(self.file -i >= 0):
                                                target_square_3 = board[self.rank + i][self.file - i]
                                                if(target_square_3.color != self.color and count_3 < 1):
                                                        if target_square_3.color != None:
                                                                count_3+=1
                                                        target_location = (self.rank + i, self.file - i)
                                                        if (not (target_location in legal_moves) ):
                                                                legal_moves.append(target_location)
                                except:
                                        pass

                                try:
                                        if(self.rank - i >= 0):
                                                target_square_4 = board[self.rank - i][self.file + i]
                                                if(target_square_4.color != self.color and count_4 < 1):
                                                        if target_square_4.color != None:
                                                                count_4+=1
                                                        target_location = (self.rank - i, self.file + i)
                                                        if (not (target_location in legal_moves) ):
                                                                legal_moves.append(target_location)
                                except:
                                        pass
                return legal_moves

