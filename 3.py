#Given an array,
# rotate the array to the right by k steps,
# where k is non-negative, implement the rotation in-place with O(1) extra space.

# Function to reverse part of array
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


# Function to rotate array to the right by k steps
def rotate_right(arr, k):
    n = len(arr)
    k = k % n   # handle k > n

    reverse(arr, 0, n - 1)      # step 1
    reverse(arr, 0, k - 1)      # step 2
    reverse(arr, k, n - 1)      # step 3


# -------- Main Program --------
arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))

rotate_right(arr, k)

print("Rotated array:", arr)