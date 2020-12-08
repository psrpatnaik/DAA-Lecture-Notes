#
# [
#     [0, 0, 1, 0],
#     [1, 0, 0, 0],
#     [0, 0, 0, 1],
#     [0, 0, X, 0]
#     [0, 0, X, 0]
# ]

# N to denote the N of Queens problem.
N = 4
# create a board of NxN size and initialize it with 0
board = [[0 for i in range(N)] for i in range(N)]

#print(board)

def check_column(board, row, column):
    for i in range(row,-1,-1):
        if board[i][column] == 1:
            return False
    return True

def check_diagonal(board, row, column):
    # diagonally moving towards top left
    for i,j in zip(range(row,-1,-1), range(column,-1,-1)):
        if board[i][j] == 1:
            return False
    # diagonally moving towards top right
    for i,j in zip(range(row,-1,-1), range(column,N)):
        if board[i][j] == 1:
            return False
    return True

# Backtracking logic

def NQueens(board, row):
    # since list of lists is zero indexed
    if row == N:
        return True
    for i in range(N):
        if (check_column(board,row,i) == True and check_diagonal(board, row, i) == True):
            board[row][i] = 1
            if NQueens(board, row + 1):
                return True
            board[row][i] = 0
    return False
# Call the NQueens
NQueens(board,0)

# Print the board
for row in board:
    print(row)

# complexity of this approach O(n!) ---- O(n^n)
# Sudoku problem