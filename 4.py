#Write a function to merge two sorted arrays into a single sorted array
#The function should handle arrays of different lengths and ensure the final array is sorted

# Function to merge two sorted arrays
def merge_sorted_arrays(arr1, arr2):
    i = 0
    j = 0
    merged = []

    # Compare elements from both arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Copy remaining elements (if any)
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged


# -------- Main Program --------
arr1 = list(map(int, input("Enter first sorted array: ").split()))
arr2 = list(map(int, input("Enter second sorted array: ").split()))

result = merge_sorted_arrays(arr1, arr2)
print("Merged sorted array:", result)