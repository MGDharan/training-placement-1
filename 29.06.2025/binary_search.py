# Filename: binary_search.py
def binary_search(sorted_list, target):
    """Performs a binary search on a sorted list."""
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1 # Target not found