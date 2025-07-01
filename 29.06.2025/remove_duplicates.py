# Filename: remove_duplicates.py
def remove_duplicates(list_):
    """Removes duplicate elements from a list while preserving order."""
    return list(dict.fromkeys(list_))