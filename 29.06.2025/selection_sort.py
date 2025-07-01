# Filename: selection_sort.py
def selection_sort(list_):
    """Sorts a list using the selection sort algorithm."""
    for i in range(len(list_)):
        min_index = i
        for j in range(i+1, len(list_)):
            if list_[min_index] > list_[j]:
                min_index = j
        list_[i], list_[min_index] = list_[min_index], list_[i]
    return list_