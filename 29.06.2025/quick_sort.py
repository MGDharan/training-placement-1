# Filename: quick_sort.py
def quick_sort(list_):
    """Sorts a list using the quick sort algorithm."""
    if len(list_) < 2:
        return list_
    else:
        pivot = list_[0]
        less = [i for i in list_[1:] if i <= pivot]
        greater = [i for i in list_[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)