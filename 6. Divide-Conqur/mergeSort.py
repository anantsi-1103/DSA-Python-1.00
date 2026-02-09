def merge_sort(arr):
    # base case 
    if len(arr)<=1:
        return arr
    
    #kaam
    mid = len(arr)//2

    # division - slice
    # recursion call
    left_sort = merge_sort(arr[:mid])
    right_sort = merge_sort(arr[mid:])


    return merge(left_sort,right_sort)


def merge(left, right):
    # temp
    result = []
    i = j = 0

    #compare kro 
    while i<len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    # remaining element
    result.extend(left[i:])
    result.extend(right[j:])

    return result

arr = [38,27,43,3,9,82,10]

print("Before Sorted : ", arr)
sorted_arr = merge_sort(arr)
print("After Sorted : ", sorted_arr)


# Time - 0(n log n)

