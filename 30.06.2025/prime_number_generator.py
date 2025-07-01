# Filename:  prime_number_generator.py
def prime_generator(limit):
    """Generates prime numbers up to a given limit."""
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num