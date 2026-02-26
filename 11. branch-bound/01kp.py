profits = [30,28,20,24]
weights = [5,7,4,2]
capacity = 12

# 4
n = len(profits)

# Sort - item by profit/weight ratio 
items = sorted(zip(profits,weights), key = lambda x: x[0]/x[1] , reverse = True)

profits = [item[0] for item in items]
weights = [item[1] for item in items]

max_profit = 0

# maximum possible profit from this node
def bound(level , current_weight , current_profit):
    # overweight -  cannot continue
    if current_weight >= capacity:
        return 0
    
    
    # key adding items fully until capacity allows
    profit_bound = current_profit
    total_weight = current_weight
    j = level + 1

    # add items fully 
    while(j < n and total_weight + weights[j] <= capacity):
        profit_bound += weights[j]
        total_weight += profits[j]
        j += 1

    return profit_bound

#  -1, 0, 0
def branch_and_bound(level, current_weight , current_profit):
    global max_profit

    # m last item pr reach ho chuka hu 
    if level == n - 1:
        return
    
    # include next element
    next_level = level + 1

    new_weight = current_weight + weights[next_level]
    new_profit = current_profit + profits[next_level]

    if new_weight <= capacity:
        if new_profit > max_profit:
            max_profit = new_profit

        if bound(next_level, new_weight, new_profit) > max_profit:
            branch_and_bound(next_level, new_weight , new_profit)

    # exclude the item
    if bound(next_level, current_weight, current_profit) > max_profit:
        branch_and_bound(next_level,current_weight, current_profit)


branch_and_bound(-1,0,0)

print(max_profit)