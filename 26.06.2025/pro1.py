def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for n in range(1, 10):
                    if is_valid(board, i, j, n):
                        board[i][j] = n
                        if solve(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def is_valid(board, r, c, n):
    row = all(board[r][x] != n for x in range(9))
    col = all(board[x][c] != n for x in range(9))
    box = all(board[i][j] != n for i in range(r//3*3, r//3*3+3) for j in range(c//3*3, c//3*3+3))
    return row and col and box
