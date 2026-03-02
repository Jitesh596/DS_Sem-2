import time

#M-1: Reccursion
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("Enter number: "))

start1 = time.time()
for i in range(n):
    print(fibo(i))
end1 = time.time()
print("Time taken (Recursion):", (end1 - start1) * 1000, "ms")

#M-2: Array
n = int(input("Enter number: "))

start2 = time.time()
arr = [0, 1]
for i in range(2, n):
    arr.append(arr[i-1] + arr[i-2])
print(arr)
end2 = time.time()
print("Time taken (Array):", (end2 - start2) * 1000, "ms")



#M-3: loop
n = int(input("Enter number: "))

start3 = time.time()
prev = 0
current = 1
for i in range(n):
    print(prev)
    temp = prev + current
    prev = current
    current = temp
end3 = time.time()
print("Time taken (Loop):", (end3 - start3) * 1000, "ms")

#Note: Start and end time is recorded for each method using time.time() and the difference (in milliseconds) is used to compare efficiency.