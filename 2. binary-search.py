# binary search

def binary_search(arr, key, low, high):
    if low > high:
        return -1  # Key not found

    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)


# ============================
# THEORY & COMPLEXITY
# ============================
# Binary Search works on the principle of Divide and Conquer
# It divides the search interval in half each time
# Time Complexity: O(log n)
# Space Complexity: O(log n) due to recursion stack
# where n is the number of elements in the array