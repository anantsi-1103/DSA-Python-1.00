# function creation
def linearSearch(list , key): #[5,4,3,8,9]
    for i in range(len(list)):
        if list[i] == key: 
            #list[4] == 10
            return i
    return -1






list = [5,4,3,5,8,9,7,6,1]
#function calling
print(linearSearch(list,1))
