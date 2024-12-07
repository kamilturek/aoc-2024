import sys

OBSTACLE = "#"
GUARD = "^"


def simulate(guard, obstacles, cols, rows):
    direction = -1j
    visited = {(guard, direction)}

    while 0 <= int(guard.real) < cols and 0 <= int(guard.imag) < rows:
        while (guard + direction) in obstacles:
            direction *= 1j

        guard += direction

        if (guard, direction) in visited:
            return True

        visited.add((guard, direction))

    return False


def solve(input):
    """
    >>> solve(open('input1.txt'))
    6
    >>> solve(open('input2.txt'))
    1618
    """
    matrix = input.read().strip().splitlines()
    cols = len(matrix)
    rows = len(matrix[0])

    obstacles = set()
    guard = None

    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            if cell == OBSTACLE:
                obstacles.add(x + y * 1j)
            elif cell == GUARD:
                guard = x + y * 1j

    total = 0

    for y in range(rows):
        for x in range(cols):
            new_obstacle = x + y * 1j

            if new_obstacle in obstacles:
                continue

            new_obstacles = obstacles.copy()
            new_obstacles.add(new_obstacle)

            if simulate(guard, new_obstacles, cols, rows):
                total += 1

    return total


if __name__ == "__main__":
    print(solve(sys.stdin))
