# Filename:  decorator_example.py
def my_decorator(func):
    """A simple decorator that prints a message before and after function execution."""
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper