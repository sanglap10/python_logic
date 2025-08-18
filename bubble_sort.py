# Array before sorting
arr = [64, 25, 12, 22, 11]

print("Original array:", arr)

# Bubble Sort
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            # Swap
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted array:", arr)