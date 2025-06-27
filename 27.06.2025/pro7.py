def josephus(n, k):
    if n == 1:
        return 0
    return (josephus(n - 1, k) + k) % n

print(josephus(7, 3))  # Position of survivor
