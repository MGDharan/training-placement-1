def solve_n_queens(n):
    res = []
    board = [-1] * n

    def is_safe(r, c):
        for i in range(r):
            if board[i] == c or abs(board[i] - c) == abs(i - r):
                return False
        return True

    def backtrack(r):
        if r == n:
            res.append(board[:])
            return
        for c in range(n):
            if is_safe(r, c):
                board[r] = c
                backtrack(r + 1)

    backtrack(0)
    return res
