def knapsack_backtracking(wt, val, capacity):
    n = len(wt)
    max_value = 0
    best_items = []

    def backtrack(i, current_weight, current_value, selected):
        nonlocal max_value, best_items

        # If capacity exceeded → stop
        if current_weight > capacity:
            return

        # If all items processed
        if i == n:
            if current_value > max_value:
                max_value = current_value
                best_items = selected.copy()
            return

        # -------- Include current item --------
        selected.append(i)
        backtrack(i + 1,
                  current_weight + wt[i],
                  current_value + val[i],
                  selected)

        selected.pop()   # BACKTRACK

        # -------- Exclude current item --------
        backtrack(i + 1,
                  current_weight,
                  current_value,
                  selected)

    backtrack(0, 0, 0, [])

    return max_value, best_items


# Driver Code
wt = [2, 3, 4, 5]
val = [3, 5, 6, 10]
M = 8

max_val, items = knapsack_backtracking(wt, val, M)

print("Maximum Value:", max_val)
print("Selected Items (W : V):")

for i in items:
    print(f"{wt[i]} : {val[i]}")
