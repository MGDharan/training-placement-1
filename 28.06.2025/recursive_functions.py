# Filename:  recursive_functions.py
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def sum_list_recursive(data):
    if not data:
        return 0
    else:
        return data[0] + sum_list_recursive(data[1:])