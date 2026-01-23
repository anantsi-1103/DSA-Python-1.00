# when a func call itself inside a func , time,space complexity reduce hojati hai 
# Recursive/Recursion -> STACK -> LIFO -> Last in first out -> add/deletion top se hoga 

# user se n , 1 --- n -> 
# 5 - 1+2+3+4+5

def sum(n): # 8
    sum = 0 # 0 1 3 6 10 15 21 28 36
    for i in range(1,n+1): #
        sum = sum + i 
        # sum = 36
    return sum

# time complexity - o(n) , space - o(1)

# Recursion -> base case , kaam

def sum_recursion(n): #5 4
    #base case
    if n == 0:
        return n
    #kaam
    return n + sum_recursion(n-1)

# time complexity - 0(n) ,  space -> call stack function ke andr 0(n)

# 5 -> 1*2*3*4*5

def fact(n): # 8
    fact = 1 # 0 1 3 6 10 15 21 28 36
    for i in range(1,n+1): #
        fact = fact * i 
        # sum = 36
    return fact

def fact_recursion(n): #5 4
    #base case
    if n == 1:
        return n
    #kaam
    return n * fact_recursion(n-1)

def count(si, ei): #10 ,  10
    if si == ei+1:
        return
    
    print(si) # 1 2 3 4 5 6 7 8 9 10
    count(si+1,ei) # 3 , 10
# 0 + 1 = 1
# 0 * 1 = 0
    
# print(sum(5))
# print(sum_recursion(5))

# print(fact(5))
# print(fact_recursion(5))

count(1,10)
