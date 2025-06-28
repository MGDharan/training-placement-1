def print_solution(sol):
    for row in sol:
        print(" ".join(str(cell) for cell in row))

def is_safe(maze, x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1

def solve_maze(maze):
    n = len(maze)
    sol = [[0 for _ in range(n)] for _ in range(n)]

    def backtrack(x, y):
        if x == n - 1 and y == n - 1:
            sol[x][y] = 1
            return True
        if is_safe(maze, x, y):
            sol[x][y] = 1
            if backtrack(x + 1, y):  # Move down
                return True
            if backtrack(x, y + 1):  # Move right
                return True
            sol[x][y] = 0  # Backtrack
        return False

    if backtrack(0, 0):
        print("Solution path (1 = path, 0 = wall or unvisited):")
        print_solution(sol)
    else:
        print("No solution exists.")

# Example Maze (1 = open path, 0 = wall)
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

solve_maze(maze)
