# Filename: lcm_calculator.py
def lcm(a, b):
    """Calculates the least common multiple (LCM) of two integers."""
    return (a * b) // gcd(a, b)