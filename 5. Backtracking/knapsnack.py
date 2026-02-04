def knapsack_backtracking(wt,val,M,n):
    # base case 
    if n == 0 or M == 0:
        return 0
    # if weight of current element is more than the capacity
    if wt[n-1] > M:
        return knapsack_backtracking(wt,val,M,n-1)
    else:
        # include - x - value = 1
        include = val[n-1] + knapsack_backtracking(wt,val,M-wt[n-1],n-1)
        # exclude - x - value = 0
        exclude = knapsack_backtracking(wt,val,M,n-1)
        return max(include,exclude)

wt = [2,3,4,5]
val = [3,5,6,10]
M = 8
n = len(wt)

result = knapsack_backtracking(wt,val,M,n)
print("Maximum Value : ", result)