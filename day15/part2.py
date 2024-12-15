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


def can_push(warehouse, pos, direction):
    if warehouse[pos] == "#":
        return False

    if warehouse[pos] == ".":
        return True

    if direction in [UP, DOWN] and warehouse[pos] in "[]":
        next_pos_1 = pos + direction
        next_pos_2 = next_pos_1 + 1 if warehouse[pos] == "[" else next_pos_1 - 1

        return can_push(warehouse, next_pos_1, direction) and can_push(
            warehouse, next_pos_2, direction
        )

    return can_push(warehouse, pos + direction, direction)


def try_push(warehouse, pos, direction):
    if warehouse[pos] == "#":
        return False

    if warehouse[pos] == ".":
        return True

    if direction in [UP, DOWN]:
        if warehouse[pos] == "[":
            if can_push(warehouse, pos + direction, direction) and can_push(
                warehouse, pos + direction + 1, direction
            ):
                try_push(warehouse, pos + direction, direction)
                try_push(warehouse, pos + direction + 1, direction)
                warehouse[pos + direction] = "["
                warehouse[pos + direction + 1] = "]"
                warehouse[pos] = "."
                warehouse[pos + 1] = "."
                return True
            else:
                return False
        elif warehouse[pos] == "]":
            if can_push(warehouse, pos + direction, direction) and can_push(
                warehouse, pos + direction - 1, direction
            ):
                try_push(warehouse, pos + direction, direction)
                try_push(warehouse, pos + direction - 1, direction)
                warehouse[pos + direction] = "]"
                warehouse[pos + direction - 1] = "["
                warehouse[pos] = "."
                warehouse[pos - 1] = "."
                return True
            else:
                return False

    if try_push(warehouse, pos + direction, direction):
        warehouse[pos + direction] = warehouse[pos]
        return True

    return False


def print_warehouse(warehouse):
    cols = max(int(pos.real) for pos in warehouse)
    rows = max(int(pos.imag) for pos in warehouse)

    for y in range(rows + 1):
        for x in range(cols + 1):
            print(warehouse[x + y * 1j], end="")
        print()


def solve(input):
    """
    >>> solve(open('input1.txt'))
    9021
    >>> solve(open('input2.txt'))
    1386070
    """
    grid, moves = input.read().split("\n\n")
    grid = grid.splitlines()
    moves = moves.replace("\n", "")

    robot = None
    warehouse = {}

    x, y = 0, 0

    for row in grid:
        x = 0

        for cell in row:
            pos = x + y * 1j

            if cell == "#":
                warehouse[pos] = "#"
                warehouse[pos + 1] = "#"
            elif cell == ".":
                warehouse[pos] = "."
                warehouse[pos + 1] = "."
            elif cell == "O":
                warehouse[pos] = "["
                warehouse[pos + 1] = "]"
            elif cell == "@":
                robot = pos
                warehouse[pos] = "@"
                warehouse[pos + 1] = "."

            x += 2
        y += 1

    for move in moves:
        direction = DIRECTIONS[move]
        next_pos = robot + direction

        if direction in [UP, DOWN] and warehouse[next_pos] in "[]":
            next_pos_1 = next_pos
            next_pos_2 = next_pos + 1 if warehouse[next_pos] == "[" else next_pos - 1

            if can_push(warehouse, next_pos_1, direction) and can_push(
                warehouse, next_pos_2, direction
            ):
                try_push(warehouse, next_pos_1, direction)
                try_push(warehouse, next_pos_2, direction)
                warehouse[next_pos_1] = "@"
                warehouse[robot] = "."
                robot = next_pos_1
        elif try_push(warehouse, next_pos, direction):
            warehouse[next_pos] = "@"
            warehouse[robot] = "."
            robot = next_pos

    return sum(
        100 * int(pos.imag) + int(pos.real)
        for pos, cell in warehouse.items()
        if cell == "["
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
