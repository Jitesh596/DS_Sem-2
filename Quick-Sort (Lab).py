def partition (arr,p,r):
    pivot = arr[r]
    i = p-1
    for j in range(p,r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1