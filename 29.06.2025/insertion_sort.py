# Filename: insertion_sort.py
def insertion_sort(list_):
    """Sorts a list using the insertion sort algorithm."""
    for i in range(1, len(list_)):
        key = list_[i]
        j = i - 1
        while j >= 0 and key < list_[j]:
            list_[j + 1] = list_[j]
            j -= 1
        list_[j + 1] = key
    return list_