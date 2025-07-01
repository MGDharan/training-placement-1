# Filename:  fibonacci_generator.py
def fibonacci_generator(limit):
    """Generates Fibonacci numbers up to a given limit."""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b