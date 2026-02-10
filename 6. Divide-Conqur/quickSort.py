def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    pivot = arr[-1] # last element pivot
    left = []
    right =[]

    for i in range(len(arr)-1):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [25, 36, 12, 4, 5, 16, 58, 54, 24, 16, 9, 65, 78]

print("Before Sorted : ", arr)
sorted_arr = quick_sort(arr)
print("After Sorted :", sorted_arr)