class Piece:
        def __init__(self, type, color, symbol, rank, file) -> None:
                self.type = type
                self.color = color
                self.symbol = symbol
                self.rank = rank
                self.file = file
                self.location = (rank, file)
                
        def __str__(self) -> str:
                return self.symbol
        def move_to(self, rank, file):
                self.rank = rank
                self.file = file
                self.location = (rank, file)
        def get_legal_moves(self, board):
                legal_moves = []
                if self.type == "Rook":
                        legal_moves.append(self.get_rook_moves(board))
                elif self.type == "Knight":
                        pass
                elif self.type == "Bishop":
                        count_1 = 0
                        count_2 = 0
                        count_3 = 0;
                        count_4 = 0;
                        
                        for i in range(8):
                                if i != 0:
                                        try:
                                                if (self.rank + i < 8 and self.rank - i >= 0 and self.file + i < 8 and self.file - i >= 0):
                                                        target_square_1 = board[self.rank + i][self.file + i]
                                                        target_square_2 = board[self.rank - i][self.file - i]
                                                        target_square_3 = board[self.rank + i][self.file - i]
                                                        target_square_4 = board[self.rank - i][self.file + i]
                                                        
                                                
                                                        if(target_square_1.color != self.color and count_1 < 1):
                                                                target_location = (self.rank + i, self.file + i)
                                                                if (not (target_location in legal_moves) ):
                                                                        if target_square_1.color != None:
                                                                                count_1+=1
                                                                        legal_moves.append(target_location)
                                                        elif(target_square_2.color != self.color and count_2 < 1):
                                                                target_location = (self.rank - i, self.file - i)
                                                                if (not (target_location in legal_moves)  ):
                                                                        if target_square_2.color != None:
                                                                                count_2+=1
                                                                        legal_moves.append(target_location)
                                                        elif(target_square_3.color != self.color and count_3 < 1):
                                                                target_location = (self.rank + i, self.file - i)
                                                                if (not (target_location in legal_moves) ):
                                                                        if target_square_3.color != None:
                                                                                count_3+=1
                                                                        legal_moves.append(target_location)
                                                        elif(target_square_4.color != self.color and count_4 < 1):
                                                                target_location = (self.rank - i, self.file + i)
                                                                if (not (target_location in legal_moves) ):
                                                                        if target_square_4.color != None:
                                                                                count_4+=1
                                                                        legal_moves.append(target_location)
                                                        else:
                                                                continue
                                                else:
                                                        continue
                                        except:
                                                pass
                elif self.type == "Queen":
                        pass
                elif self.type == "King":
                        pass
                return legal_moves
        
        def get_rook_moves(self, board):
                legal_moves = []
                for i in range(8):
                        for j in range(8):
                                try:
                                        target_square = board[i][j]
                                        if (board[self.file + i][self.rank].color == self.color or board[self.file][self.rank+j].color == self.color or board[self.file-i][self.rank].color == self.color or board[self.file][self.rank-j].color == self.color):
                                                return legal_moves;
                                        elif((target_square == self.EMPTY or target_square.color != self.color) and (not ((i, j) in legal_moves)) and (i == self.rank or j == self.file) and not (i == self.rank and j == self.file)):
                                                legal_moves.append((i, j))
                                except:
                                        pass
                return legal_moves