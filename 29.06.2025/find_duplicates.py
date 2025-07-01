# Filename: find_duplicates.py
def find_duplicates(list_):
    """Finds and returns duplicate elements from a list."""
    seen = set()
    duplicates = set()
    for item in list_:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)