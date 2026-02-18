import sys

def dijkstra(graph, source):
    
    # Step 1: Initialize distances with maximum value
    dist = {node: sys.maxsize for node in graph}
    dist[source] = 0

    # Step 2: Set to store (distance, node)
    st = set()
    st.add((0, source))

    # Step 3: Process until set is empty
    while st:
        #  1, 5 
        curr_dist, u = min(st) 
        st.remove((curr_dist, u))

        # Step 4: Relax adjacent nodes
        for v, weight in graph[u]:
            if curr_dist + weight < dist[v]:

                # Remove old pair if present
                if dist[v] != sys.maxsize:
                    st.discard((dist[v], v))

                # Update distance
                dist[v] = curr_dist + weight
                st.add((dist[v], v))

    return dist


graph = {
    0: [(1,5),(2,8)],
    1: [(3,2),(0,5),(2,9)],
    2: [(1,9),(3,6),(0,8)],
    3: [(1,2),(2,6)]
}
# 0 5 8 7
result = dijkstra(graph,0)

for node in sorted(result):
    print(f"{node} - {result[node]}")

