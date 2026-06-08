import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    open_list = [(0, start)]
    came_from = {start: None}
    g = {start: 0}

    while open_list:
        _, cur = heapq.heappop(open_list)

        if cur == goal:
            path = []
            while cur:
                path.append(cur)
                cur = came_from[cur]
            return path[::-1]

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nb = (cur[0] + dx, cur[1] + dy)

            if (0 <= nb[0] < len(grid) and
                0 <= nb[1] < len(grid[0]) and
                grid[nb[0]][nb[1]] == 0):

                ng = g[cur] + 1

                if nb not in g or ng < g[nb]:
                    g[nb] = ng
                    heapq.heappush(
                        open_list,
                        (ng + heuristic(nb, goal), nb)
                    )
                    came_from[nb] = cur

    return None


grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

path = astar(grid, (0, 0), (4, 4))
print("Path:", path)