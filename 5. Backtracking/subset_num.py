def subset(num):
    result = []
    
    def backtrack(index,path):
        result.append(path.copy())

        for i in range(index , len(num)):
            path.append(num[i])
            backtrack(i+1,path)
            path.pop() #backtrack


    backtrack(0,[])
    return result
    

print(subset([1,2]))