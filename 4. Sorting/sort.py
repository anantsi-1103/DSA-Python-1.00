def bubble_sort(list):
    n = len(list)

    for i in range(n): # n
        for j in range(0,n-i-1): # n
            if list[j]>list[j+1]:
                # < will convert in des order
                #swap
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

                # n^2

def selectionSort(arr):
    n = len(arr)

    for i in range(n-1):
        min_index = i

        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j

        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index]=temp

def insertionSort(arr):
    n = len(arr)

    for i in range(1,n):
        key = arr[i]
        j = i-1

        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j = j-1
            
        arr[j+1] = key

    return arr


list = [5,4,3,1,2]
arr = [5,4,3,1,2]

# print(list)
# bubble_sort(list)
# print(list)


print(arr)
selectionSort(arr)
print(arr)