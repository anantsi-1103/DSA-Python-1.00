from collections import deque

# Graph representation using adjacency list
graph = {
    0: [3],
    3: [0, 1],
    1: [2 ,3, 4],
    2: [1],
    4: [1]
}

def bfs(graph, start):
    visited = set()
    queue = deque()

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Run BFS
bfs(graph, 0)
