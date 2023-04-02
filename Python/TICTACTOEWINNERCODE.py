def returnWinner(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return -1

a = [['X', 'O', 'X'],
     ['O', 'X', 'O'],
     ['O', 'X', 'O']]

print(returnWinner(a))
