def pallindrome_rec(n , sum=0):
    if(n == 0):
        return sum
    return pallindrome_rec(n//10, sum*10 + n % 10)
                        # 153, 3
                        # 15 , 3
                        # 1 , 35
                        # 0, 351
    
def armstrong(n,d):
    if n == 0:
        return n
    return (n % 10) ** d + armstrong(n // 10 , d)
    # 27 + (f(15), 3)
    # 125 + (f(1),3)
    # 1 + ((f(0) , 3))
    # 0

def count_digit(n): # 153 
    if n == 0:
        return 0
    return 1 + count_digit(n//10)
    # 1 + f(15)
    # 1 + f(1)
    # 1 + f(0)
    # 0

def isprime(n,i=2): #5 , 2-3
    if n <= 2:
        return n == 2
    # 4 % 2 == 0
    if n % i == 0:
        return False
    
    # 3  * 3   > 5
    if i * i > n:
        return True
    
    return isprime(n , i+1)




num = int(input("Enter the number you want to check!!!\n"))
# digit = count_digit(num)


# if armstrong(num,digit) == num:
#     print("Yes")
# else:
#     print("No")


# num = int(input("Enter the number you want to check!!!\n"))
# if num == pallindrome_rec(num):
#     print("Yes")
# else:
#     print("No")


