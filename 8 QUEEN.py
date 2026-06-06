def solve_n_queens(n):
    solutions = []

    def safe(positions, row, col):
        for r in range(row):
            c = positions[r]
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def search(row, positions):
        if row == n:
            solutions.append(positions[:])
            return

        for col in range(n):
            if safe(positions, row, col):
                positions[row] = col
                search(row + 1, positions)

    search(0, [-1] * n)
    return solutions


n = 8
solutions = solve_n_queens(n)

print("Total Solutions =", len(solutions))

print("\nFirst Solution (8x8 Board):\n")

board = solutions[0]

for row in range(n):
    for col in range(n):
        if board[row] == col:
            print(" Q ", end="")
        else:
            print(" . ", end="")
    print()