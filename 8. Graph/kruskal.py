
class DisjoinSet:
    def __init__(self,n):
        # parent[i] = each of node i
        # each node is parent of itself
        self.parent = {i : i for i in range(1,n+1)}

        # rank is used so - 0
        self.rank = {i:0 for i in range(1, n+1)}

    # root of the node
    def find(self, x):
        # if x is not its parent
        if self.parent[x] != x:
            # directly attach to its root
            # path compression
            # 3 -> 2 -> 1
            self.parent[x] = self.find(self.parent[x])


        return self.parent[x]
    

    def union(self,x,y):
        # find root
        rootX = self.find(x) # 1
        rootY = self.find(y) # 4

        # if both have same root 
        if rootX == rootY:
            return False
        
        # attach smaller rank tree under a larger rank tree
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY

        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX

        else:
            # if same rank 
            self.parent[rootY] = rootX
            self.rank[rootX]+=1

        return True
        
def krushkal(vertices, edges):
    
    # sort edges based on weight
    edges.sort(key = lambda x : x[2])

    # Create disjoint set for vertices
    ds = DisjoinSet(vertices)


    mst = [] # store mst edges
    cost = 0  # total weight mst 


    # process edges one by one
    for u,v,w in edges:

        # try to connect u and v
        if ds.union(u,v):
            # if no cycle include in the edges - diff component 
            mst.append((u,v,w))
            cost += w

    return mst, cost


edges = [
    (4,1,1),
    (1,2,2),
    (4,2,3),
    (3,2,3),
    (5,1,4),
    (4,3,5),
    (2,6,7),
    (3,6,8),
    (5,4,9)
]

mst , cost = krushkal(6, edges)


print("MST: ", mst)
print("Cost: ", cost)