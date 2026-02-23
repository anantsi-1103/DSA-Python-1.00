
def fractional_knapsnack(profit ,  weight , capacity):
    n = len(profit)

    # create list of items (profit ,  weight , ratio)
    items =[]

    for i in range(n):
        ratio = profit[i] / weight[i]
        items.append((profit[i] , weight[i] , ratio))


    # Sort items by ratio in descending Order
    items.sort(key = lambda x : x[2] , reverse= True)

    total_profit = 0.0

    print("Selected Items")

    for p,w,r in items:
        if capacity >= w:
            # take full item
            capacity -= w
            total_profit += p
            print(f"Take Full item -> Profit : {p}, Weight : {w}")
        else:
            # Take Fractional Part
            fraction = capacity/w
            total_profit += p * fraction
            print(f"Take {fraction : .2f} part of item -> profit : {p * fraction: .2f}")
            break

    return total_profit






profit = [25,24,15]
weight = [18,15,10]
capacity = 20

max_profit = fractional_knapsnack(profit , weight , capacity)

print("\n Maximum Profit : ", round(max_profit,2))