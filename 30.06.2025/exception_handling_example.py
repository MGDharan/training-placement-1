# Filename:  exception_handling_example.py
def divide(x, y):
  """Divides two numbers and handles potential ZeroDivisionError."""
  try:
    result = x / y
    return result
  except ZeroDivisionError:
    return "Division by zero!"