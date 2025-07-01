# Filename: gcd_calculator.py
def gcd(a, b):
    """Calculates the greatest common divisor (GCD) of two integers using Euclid's algorithm."""
    while(b):
        a, b = b, a % b
    return a