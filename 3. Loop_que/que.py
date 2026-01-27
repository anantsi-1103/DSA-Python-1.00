def pallindrome(n): # 153
    #153 
    temp = n
    cal = 0
    while(temp != 0):
        # extract last digit
        digit = temp % 10
        # sum krke store kr rha hai
        cal = cal * 10 + digit
        # short
        temp = temp // 10

    if(cal == n):
        # 351 == 153 
        return "Pallindrome Number"
    else:
        return "Not a Pallindrome Number"

def armstrong(n): # 153
    #153 
    temp = n
    sum = 0
    while(temp != 0):
        # extract last digit
        digit = temp % 10
        # sum krke store kr rha hai
        sum = sum+ digit ** 3
        # short
        temp = temp // 10

    if(sum == n):
        # 351 == 153 
        return "Armstrong Number"
    else:
        return "Not a Armstrong Number"  
    
def prime(n):

    if n <= 1:
        return False
    
    i = 2 
    count=0
    while(i<=n):
        if(n % i == 0):
            count += 1
        i+=1

    if(count == 1):
        return True
    else:
        return False
    


print(prime(10))