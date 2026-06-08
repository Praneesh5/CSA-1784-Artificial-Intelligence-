from collections import deque

def bfs(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()

        if node == end:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append((neighbour, path + [neighbour]))

    return None


graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2, 4],
    4: [3]
}

path = bfs(graph, 0, 4)
print(f"Shortest path: {path}")