from collections import deque

def solve_water_jug(jug1, jug2, target):

    q = deque()
    q.append((0, 0, []))

    visited_states = set()

    while q:

        j1, j2, path = q.popleft()

        if (j1, j2) in visited_states:
            continue

        visited_states.add((j1, j2))

        if j1 == target:
            return path + [f"Goal Reached: ({j1}, {j2})"]

        next_states = [
            (jug1, j2, "Fill Jug-1"),
            (j1, jug2, "Fill Jug-2"),
            (0, j2, "Empty Jug-1"),
            (j1, 0, "Empty Jug-2")
        ]

        transfer = min(j1, jug2 - j2)
        next_states.append(
            (j1 - transfer, j2 + transfer, "Transfer Jug-1 → Jug-2")
        )

        transfer = min(jug1 - j1, j2)
        next_states.append(
            (j1 + transfer, j2 - transfer, "Transfer Jug-2 → Jug-1")
        )

        for nj1, nj2, action in next_states:
            q.append((nj1, nj2, path + [f"{action}  =>  ({nj1}, {nj2})"]))

    return None


result = solve_water_jug(4, 3, 2)

if result:
    print("Water Jug Solution\n")
    for step_no, action in enumerate(result, start=1):
        print(f"Step {step_no}: {action}")
else:
    print("Solution does not exist.")