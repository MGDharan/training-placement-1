# Filename:  list_comprehension_example.py
def square_even(numbers):
    """Squares only the even numbers in a list using list comprehension."""
    return [x**2 for x in numbers if x % 2 == 0]