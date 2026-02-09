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


arr = [10,7,8,9,1,5]

print("Before Sorted : ", arr)
sorted_arr = quick_sort(arr)
print("After Sorted :", sorted_arr)