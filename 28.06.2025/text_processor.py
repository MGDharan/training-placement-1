# Filename:  text_processor.py
import re

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text) #remove punctuation
    text = text.lower()
    text = ' '.join(text.split()) #remove extra spaces
    return text

def count_words(text):
    words = text.split()
    return len(words)