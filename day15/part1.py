import sys

LEFT = -1
UP = -1j
RIGHT = 1
DOWN = 1j

DIRECTIONS = {
    "<": LEFT,
    "^": UP,
    ">": RIGHT,
    "v": DOWN,
}

ROBOT = "@"
WALL = "#"
FREE = "."
BOX = "O"


def try_push(warehouse, pos, direction):
    if warehouse[pos] == WALL:
        return False

    if warehouse[pos] == FREE:
        return True

    if try_push(warehouse, pos + direction, direction):
        warehouse[pos + direction] = warehouse[pos]
        return True

    return False


def solve(input):
    """
    >>> solve(open('input1.txt'))
    10092
    >>> solve(open('input2.txt'))
    1414416
    """
    grid, moves = input.read().split("\n\n")
    grid = grid.splitlines()
    moves = moves.replace("\n", "")

    robot = None
    warehouse = {}

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            pos = x + y * 1j
            warehouse[pos] = cell

            if cell == ROBOT:
                robot = pos

    for move in moves:
        direction = DIRECTIONS[move]

        if try_push(warehouse, robot + direction, direction):
            warehouse[robot + direction] = ROBOT
            warehouse[robot] = "."
            robot += direction

    return sum(
        100 * int(pos.imag) + int(pos.real)
        for pos, cell in warehouse.items()
        if cell == BOX
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
