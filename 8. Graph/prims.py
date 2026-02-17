import sys

graph = {
    0: [(1,2), (3,6)],
    1: [(0,2), (2,3), (4,5), (3,8)],
    2: [(1,3), (4,7)],
    3: [(0,6), (1,8)],
    4: [(1,5), (2,7)]
}

def minKey(key, mst_set):
    minimum = sys.maxsize
    min_index = -1

    for i in range(len(key)):
        if key[i] < minimum and mst_set[i] == False:
            minimum = key[i]
            min_index = i

    return min_index


def prim_mst(graph):
    V = len(graph)

    key = [sys.maxsize] * V
    parent = [-1] * V
    mst_set = [False] * V

    key[0] = 0
    parent[0] = -1

    for _ in range(V):
        u = minKey(key, mst_set)
        mst_set[u] = True

        for v, weight in graph[u]:
            if mst_set[v] == False and weight < key[v]:
                key[v] = weight
                parent[v] = u

    print_mst(parent, key)


def print_mst(parent, key):
    print("Edge    Weight")
    total = 0

    for i in range(1, len(parent)):
        print(f"{parent[i]} - {i}    {key[i]}")
        total += key[i]

    print("Total Cost:", total)


prim_mst(graph)
