def fibonacci_sequence_generator(n):
    """
    Generates a Fibonacci sequence up to n terms.
    """
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


class FileProcessor:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_file_lines(self):
        try:
            with open(self.filepath, 'r') as file:
                lines = file.readlines()
                return [line.strip() for line in lines]
        except FileNotFoundError:
            return None

    def write_to_file(self, content):
        try:
            with open(self.filepath, 'w') as file:
                file.write(content)
            return True
        except IOError:
            return False



def analyze_text(text):
    word_counts = {}
    for word in text.lower().split():
        cleaned_word = ''.join(c for c in word if c.isalnum())
        if cleaned_word:
            word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1
    return word_counts



class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance



def prime_number_checker(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


class ShapeCalculator:
    def __init__(self, shape_type, dimensions):
        self.shape_type = shape_type
        self.dimensions = dimensions

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.dimensions[0] * self.dimensions[1]
        elif self.shape_type == "circle":
            return 3.14159 * (self.dimensions[0] ** 2)
        else:
            return None

    def calculate_perimeter(self):
        if self.shape_type == "rectangle":
            return 2 * (self.dimensions[0] + self.dimensions[1])
        elif self.shape_type == "circle":
            return 2 * 3.14159 * self.dimensions[0]
        else:
            return None



def is_palindrome(text):
    processed_text = ''.join(c for c in text.lower() if c.isalnum())
    return processed_text == processed_text[::-1]


class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id, quantity):
        self.inventory[item_id] = self.inventory.get(item_id, 0) + quantity

    def remove_item(self, item_id, quantity):
        if item_id in self.inventory and self.inventory[item_id] >= quantity:
            self.inventory[item_id] -= quantity
            if self.inventory[item_id] == 0:
                del self.inventory[item_id]
            return True
        return False

    def check_stock(self, item_id):
        return self.inventory.get(item_id, 0)


def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)