# Filename:  custom_exception.py
class MyCustomError(Exception):
    """A custom exception class."""
    pass

def my_function():
    raise MyCustomError("Something went wrong!")