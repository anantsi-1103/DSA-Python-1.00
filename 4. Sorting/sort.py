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

    
list = [5,4,3,1,2]

print(list)
bubble_sort(list)
print(list)