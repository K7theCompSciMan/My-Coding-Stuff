class AI{
        def __init__(self, board):
                self.board = board
                self.bestMove = None
                self.bestMoveScore = 0
                self.currentEval = 0
                self.fake_board = Board()
        def search(self, depth) -> (int, int):
                self.minimax(depth, self.board.white_to_move)
                return self.bestMove
                
        def minimax(self, depth, maximizingPlayer):
                if depth == 0:
                        return self.evaluate()
                if maximizingPlayer:
                        maxEval = -999999
                        for move in self.board.get_legal_moves():
                                self.fake_board.piece_board = self.board.piece_board
                                self.fake_board.make_move(move)
                                eval = self.minimax(depth - 1, False)
                                if eval > maxEval:
                                        maxEval = eval
                                        if depth == 3:
                                                self.bestMove = move
                                                self.bestMoveScore = eval
                        return maxEval
                else:
                        minEval = 999999
                        for move in self.fake_board.get_legal_moves():
                                self.fake_board.piece_board = self.board.piece_board
                                self.fake_board.make_move(move)
                                eval = self.minimax(depth - 1, True)
                                if eval < minEval:
                                        minEval = eval
                                        if depth == 3:
                                                self.bestMove = move
                                                self.bestMoveScore = eval
                        return minEval
        def evaluate(self):
                self.currentEval = 0
                for row in range(8):
                        for col in range(8):
                                piece = self.board.get_piece(row, col)
                                if piece != None:
                                        self.currentEval += piece.get_value()
                return self.currentEval
}