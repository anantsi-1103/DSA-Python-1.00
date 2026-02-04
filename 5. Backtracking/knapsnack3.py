def knapsack_bt(i, wt, val, capacity):
    # Base case
    if i == len(wt) or capacity == 0:
        return 0

    # If item too heavy → skip it
    if wt[i] > capacity:
        return knapsack_bt(i + 1, wt, val, capacity)

    # Choice 1 → Take item
    take = val[i] + knapsack_bt(i + 1, wt, val, capacity - wt[i])
    # Choice 2 → Skip item
    skip = knapsack_bt(i + 1, wt, val, capacity)
    return max(take, skip)
# Driver code
wt = [2, 3, 4, 5]
val = [3, 5, 6, 10]
M = 8

ans = knapsack_bt(0, wt, val, M)
print("Maximum Value:", ans)
