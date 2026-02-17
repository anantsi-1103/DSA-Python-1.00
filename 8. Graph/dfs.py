graph = {
    0 : [2],
    1 : [2,3],
    2 : [0,1,4],
    3 : [1,4],
    4 : [2,3]
}

def dfs(graph , node , visited):
    visited.add(node)
    print(node, end=" ")

    # dubara function 
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)



visited = set()
dfs(graph, 0, visited)