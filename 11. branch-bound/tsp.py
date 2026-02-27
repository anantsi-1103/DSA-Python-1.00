import sys

N = 4

cost = [[sys.maxsize,10,15,20],
        [10, sys.maxsize,35,25],
        [15,35,sys.maxsize,30],
        [20,25,30,sys.maxsize]
        ]

visited = [False] * N
min_cost = sys.maxsize  # 95

def tsp(curr_city , count , curr_cost):
    global min_cost

    # if all cities visited -> 
    if count == N and cost[curr_city][0]:
        #  inf , 95
        min_cost = min(min_cost , curr_cost + cost[curr_city][0])
        return 
    
    # branching 
    for i in range(N):
            # 0 - 1 , 0 - 2 , 0 - 3
        if not visited[i] and cost[curr_city][i] != sys.maxsize:
            # 1 - 2, 1-3
            temp = curr_cost + cost[curr_city][i]


            # 0 -> 3 -> 2 = 50 
            #  50 + 35 = 85 > 80 
            # pruning
            # path already - temp < mincost -> 
            if temp < min_cost:

                # okay - visited kro next city 
                visited[i] = True
                tsp(i , count+1 , temp)
                visited[i] = False


visited[0] = True
tsp(0,1,0)

print(min_cost)