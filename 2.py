#Given an array of integers, perform the following operations:
# reverse the arrey,
# find the maximum and minimum elements,
# calculate the sum and average of the elements.
# Implement functions to perform each operation and ensure the time complexity is optimal.

# Function to reverse the array
def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return arr


# Function to find maximum element
def find_max(arr):
    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x
    return max_val


# Function to find minimum element
def find_min(arr):
    min_val = arr[0]
    for x in arr:
        if x < min_val:
            min_val = x
    return min_val


# Function to calculate sum
def find_sum(arr):
    total = 0
    for x in arr:
        total += x
    return total


# Function to calculate average
def find_average(arr):
    total = find_sum(arr)
    return total / len(arr)


# -------- Main Program --------
arr = list(map(int, input("Enter array elements: ").split()))

print("Reversed array:", reverse_array(arr.copy()))
print("Maximum element:", find_max(arr))
print("Minimum element:", find_min(arr))
print("Sum of elements:", find_sum(arr))
print("Average of elements:", find_average(arr))