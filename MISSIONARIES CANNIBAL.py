from collections import deque

def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False
    return True

def bfs():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([(start, [start])])
    visited = set([start])

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    while queue:
        (m, c, b), path = queue.popleft()

        if (m, c, b) == goal:
            return path

        for dm, dc in moves:
            if b == 1:
                nm, nc, nb = m - dm, c - dc, 0
            else:
                nm, nc, nb = m + dm, c + dc, 1

            if is_valid(nm, nc) and (nm, nc, nb) not in visited:
                visited.add((nm, nc, nb))
                queue.append(((nm, nc, nb), path + [(nm, nc, nb)]))

    return None

solution = bfs()

if solution:
    print("Solution found:")
    for state in solution:
        print(state)
else:
    print("No solution found.")