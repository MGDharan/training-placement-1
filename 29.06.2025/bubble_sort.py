# Filename: bubble_sort.py
def bubble_sort(list_):
    """Sorts a list using the bubble sort algorithm."""
    n = len(list_)
    for i in range(n-1):
        for j in range(n-i-1):
            if list_[j] > list_[j+1]:
                list_[j], list_[j+1] = list_[j+1], list_[j]
    return list_