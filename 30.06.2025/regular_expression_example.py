# Filename:  regular_expression_example.py
import re
def find_email(text):
    """Finds and returns email addresses from a given text using regular expressions."""
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, text)
    return emails