N = 8
moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]

def is_valid(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def solve_knight():
    board = [[-1 for _ in range(N)] for _ in range(N)]
    board[0][0] = 0

    def backtrack(x, y, movei):
        if movei == N * N:
            return True
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, board):
                board[nx][ny] = movei
                if backtrack(nx, ny, movei + 1):
                    return True
                board[nx][ny] = -1
        return False

    if backtrack(0, 0, 1):
        for row in board:
            print(row)
    else:
        print("No solution found")
