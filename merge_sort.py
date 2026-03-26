# sorting/merge_sort.py
"""
Merge Sort (stable, not in-place)
Complexity: O(n log n) worst/average/best
Stable: Yes
In-place: No (this implementation returns a new list)
"""

from typing import List

def merge(left: List[int], right: List[int]) -> List[int]:
    i = j = 0
    out = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    if i < len(left):
        out.extend(left[i:])
    if j < len(right):
        out.extend(right[j:])
    return out

def merge_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    if n <= 1:
        return arr[:]  # return a shallow copy
    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)