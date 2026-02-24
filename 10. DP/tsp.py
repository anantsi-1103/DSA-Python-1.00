
def tsp(cost):
    n = len(cost)
    #  2 ** 4 -> 16
    totalStates = 2**n 

    dp = [[-1] * n for _ in range(totalStates)]

    def dfs(mask , city):
        # if all cities Visited
        if mask ==(2 ** n) -1:
            # 15
            return cost[city][0]
        
        if dp[mask][city] != -1:
            return dp[mask][city]
        
        best = float('inf')

        for next_city in range(n):
            if(mask & (2 ** next_city)) == 0:
                new_cost = cost[city][next_city] + dfs(mask + (2 ** next_city), next_city)

                best = min(best , new_cost)


        dp[mask][city] = best
        return best
    
    return dfs(1,0)

cost = [[0,10,15,20],
        [5,0,25,10],
        [15,30,0,5],
        [15,10,20,0]]


print("Minimum Cost : ", tsp(cost))
        


