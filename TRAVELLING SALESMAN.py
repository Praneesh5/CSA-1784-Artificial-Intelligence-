import numpy as np

def tsp(cities):
    n = len(cities)

    dist = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i != j:
                dist[i][j] = np.linalg.norm(
                    np.array(cities[i]) - np.array(cities[j])
                )

    tour = [0]
    unvisited = set(range(1, n))
    total = 0

    while unvisited:
        cur = tour[-1]
        nearest = min(unvisited, key=lambda c: dist[cur][c])

        tour.append(nearest)
        unvisited.remove(nearest)
        total += dist[cur][nearest]

    tour.append(0)
    total += dist[tour[-2]][0]

    return tour, round(total, 2)


cities = [(0, 0), (1, 3), (4, 3), (6, 1), (3, 0)]

tour, distance = tsp(cities)

print("Tour:", tour)
print("Total distance:", distance)