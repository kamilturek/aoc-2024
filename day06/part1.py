import sys

OBSTACLE = "#"
GUARD = "^"


def solve(input):
    """
    >>> solve(open('input1.txt'))
    41
    >>> solve(open('input2.txt'))
    4778
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

    direction = -1j
    visited = {guard}

    while 0 <= int(guard.real) < cols and 0 <= int(guard.imag) < rows:
        while (guard + direction) in obstacles:
            direction *= 1j

        guard += direction
        visited.add(guard)

    return len(visited) - 1


if __name__ == "__main__":
    print(solve(sys.stdin))
