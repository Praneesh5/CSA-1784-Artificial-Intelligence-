from queue import PriorityQueue

graph = [[] for _ in range(14)]

def add_edge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))

edges = [
    (0,1,3), (0,2,6), (0,3,5),
    (1,4,9), (1,5,8),
    (2,6,12), (2,7,14),
    (3,8,7),
    (8,9,5), (8,10,6),
    (9,11,1), (9,12,10), (9,13,2)
]

for edge in edges:
    add_edge(*edge)

def best_first_search(src, target):
    visited = [False] * 14

    pq = PriorityQueue()
    pq.put((0, src))

    visited[src] = True

    while not pq.empty():
        cost, u = pq.get()

        print(u, end=" ")

        if u == target:
            break

        for v, edge_cost in graph[u]:
            if not visited[v]:
                visited[v] = True
                pq.put((edge_cost, v))

    print()

best_first_search(0, 9)