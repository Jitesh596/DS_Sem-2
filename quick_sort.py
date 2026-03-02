# sorting/quick_sort.py
"""
QuickSort using Lomuto partition (last element as pivot).
Complexity:
 - Average: O(n log n)
 - Worst-case: O(n^2) (e.g., already sorted with this pivot strategy)
Stable: No
In-place: Yes
Note: recursive; for large degenerate inputs adjust recursionlimit when running.
"""

from typing import List

def _lomuto_partition(arr: List[int], lo: int, hi: int) -> int:
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # place pivot after last smaller element
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1

def _quick_sort_inplace(arr: List[int], lo: int, hi: int) -> None:
    if lo < hi:
        p = _lomuto_partition(arr, lo, hi)
        _quick_sort_inplace(arr, lo, p - 1)
        _quick_sort_inplace(arr, p + 1, hi)

def quick_sort(arr: List[int]) -> None:
    """
    In-place quicksort; sorts arr ascending.
    """
    if len(arr) <= 1:
        return
    _quick_sort_inplace(arr, 0, len(arr) - 1)