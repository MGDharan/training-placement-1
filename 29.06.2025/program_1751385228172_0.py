def analyze_text_sentiment(text):
    """
    Analyzes the sentiment of a given text using VADER.
    """
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    return scores


class FibonacciSequenceGenerator:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result



def find_prime_factors(num):
    """
    Finds all prime factors of a given number.
    """
    i = 2
    factors = []
    while i * i <= num:
        while num % i == 0:
            factors.append(i)
            num //= i
        i += 1
    if num > 1:
        factors.append(num)
    return factors



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


def calculate_geometric_mean(numbers):
    """
    Calculates the geometric mean of a list of numbers.
    """
    import math
    product = 1
    for num in numbers:
        product *= num
    return math.pow(product, 1.0 / len(numbers))


class EmailValidator:
    def __init__(self, email):
        self.email = email

    def validate(self):
        import re
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        match = re.match(pattern, self.email)
        return bool(match)


def generate_random_password(length=12):
  import random
  import string
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for i in range(length))
  return password