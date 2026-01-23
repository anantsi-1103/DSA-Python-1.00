# function creation
def linearSearch(list , key): #[5,4,3,8,9]
    for i in range(len(list)):
        if list[i] == key: 
            #list[4] == 10
            return i
    return -1

# binary search = list -> sorted 
def binarySearch(list, key):
    si = 0
    ei = len(list)-1

    while(si <= ei):
        mid = (si+ei)//2

    # exact mid pr hi 
        if list[mid] == key:
            return mid
    # mid less than hua key se
        elif list[mid] < key:
            si = mid + 1
    # mid is greater than your key
        else:
            ei = mid - 1
    return -1


# list = [5,4,3,5,8,9,7,6,1]
# #function calling
# print(linearSearch(list,1))

list = [2,4,6,8,10,12,14,18,20]

# print(binarySearch(list,200))

result = binarySearch(list,10)

if(result == -1):
     print("Element not found")
else:
    print("Element found at index ",result)


# best case -> 0(1) -> Omega
#Average case -> 0(log n) -> Theta
#worst Case -> 0(log n) --- Big O

#space -> 0(1)