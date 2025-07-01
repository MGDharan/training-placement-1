# Filename: merge_sort.py
def merge_sort(list_):
    """Sorts a list using the merge sort algorithm."""
    if len(list_) <= 1:
        return list_
    mid = len(list_) // 2
    left = merge_sort(list_[:mid])
    right = merge_sort(list_[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged