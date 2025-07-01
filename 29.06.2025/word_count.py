# Filename: word_count.py
def count_words(text):
    """Counts the frequency of words in a given text."""
    words = text.lower().split()
    word_counts = {}
    for word in words:
        word = word.strip('.,!?"').replace("'s","") #basic punctuation removal
        if word:
            word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts