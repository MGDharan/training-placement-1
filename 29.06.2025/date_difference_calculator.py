# Filename: date_difference_calculator.py
from datetime import date
def days_between(d1, d2):
    """Calculates the number of days between two dates."""
    d1 = date.fromisoformat(d1)
    d2 = date.fromisoformat(d2)
    return abs((d2 - d1).days)