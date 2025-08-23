def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j  
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [10,50,8,100,12,5,60,2,0]
result = selection_sort(arr)

print(result)
