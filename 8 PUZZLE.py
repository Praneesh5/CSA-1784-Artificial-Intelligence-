import random
from queue import PriorityQueue

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def is_solvable(state):
    arr = [x for x in state if x != 0]
    inversions = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1

    return inversions % 2 == 0

def generate_puzzle():
    while True:
        puzzle = list(range(9))
        random.shuffle(puzzle)

        if is_solvable(tuple(puzzle)):
            return tuple(puzzle)

def heuristic(state):
    distance = 0

    for i in range(9):
        tile = state[i]

        if tile != 0:
            goal_row = (tile - 1) // 3
            goal_col = (tile - 1) % 3

            row = i // 3
            col = i % 3

            distance += abs(goal_row - row) + abs(goal_col - col)

    return distance

def successors(state):
    result = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    moves = []

    if row > 0:
        moves.append(-3)

    if row < 2:
        moves.append(3)

    if col > 0:
        moves.append(-1)

    if col < 2:
        moves.append(1)

    for move in moves:
        new_blank = blank + move

        s = list(state)

        s[blank], s[new_blank] = s[new_blank], s[blank]

        result.append(tuple(s))

    return result

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()

def solve(start):
    frontier = PriorityQueue()

    frontier.put((heuristic(start), 0, start))

    parent = {}

    g_cost = {start: 0}

    visited = set()

    while not frontier.empty():

        _, g, current = frontier.get()

        if current == GOAL:

            path = []

            while current in parent:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            return path

        visited.add(current)

        for nxt in successors(current):

            new_g = g + 1

            if nxt not in g_cost or new_g < g_cost[nxt]:

                g_cost[nxt] = new_g

                f = new_g + heuristic(nxt)

                frontier.put((f, new_g, nxt))

                parent[nxt] = current

    return None

initial_state = generate_puzzle()

print("\nRandom Puzzle Generated:\n")
print_board(initial_state)

solution = solve(initial_state)

if solution:

    print("Solution Found!\n")

    for step, state in enumerate(solution):

        print("Step", step)
        print_board(state)

    print("Total Moves =", len(solution) - 1)

else:
    print("No Solution Exists")