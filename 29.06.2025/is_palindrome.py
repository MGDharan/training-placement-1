# Filename: is_palindrome.py
def is_palindrome(text):
    """Checks if a given string is a palindrome (ignoring case and non-alphanumeric characters)."""
    processed_text = ''.join(c for c in text.lower() if c.isalnum())
    return processed_text == processed_text[::-1]