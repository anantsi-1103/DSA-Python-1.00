def backtrack(n):
    if n > 5:
        return 
    
    print(n)
    backtrack(n+1)
    print(n-2)


backtrack(1)