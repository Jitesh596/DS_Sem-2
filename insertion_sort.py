# sorting/insertion_sort.py
"""
Insertion Sort (in-place, stable)
Complexity: O(n^2) worst/average, O(n) best (already sorted).
Stable: Yes
In-place: Yes
"""
from typing import List

def insertion_sort(arr: List[int]) -> None:
    """
    In-place insertion sort that sorts arr ascending.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # shift elements greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key