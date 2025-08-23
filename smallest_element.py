arr = [90,10,100,20,80]
smallest = arr[0]

length = len(arr)
for i in range(length):
    index = 0
    for j in range(length):
        if arr[j] < smallest:
            smallest = arr[j]
            index = j 

print(f"Smallest element = {smallest}")
print(f"Index of the smallest element = {index}")