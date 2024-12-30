import sys
from collections import deque

LEFT = -1
UP = -1j
RIGHT = 1
DOWN = 1j

MOVES = (LEFT, UP, RIGHT, DOWN)


def get_neighbours(pos):
    return (pos + move for move in MOVES)


def get_cheats(pos):
    return (pos + move for move in (-2, -2j, 2, 2j))


def solve(input):
    """
    >>> solve(open('input2.txt'))
    1402
    """
    start = None
    racetrack = {}

    for y, row in enumerate(input):
        for x, cell in enumerate(row.strip()):
            pos = x + y * 1j

            if cell == "#":
                continue

            if cell == "S":
                start = pos

            racetrack[pos] = cell

    distances = {start: 0}
    queue = deque([(start, 0)])

    while len(queue) > 0:
        curr_pos, curr_dist = queue.popleft()

        for neighbour in get_neighbours(curr_pos):
            if neighbour in distances or neighbour not in racetrack:
                continue

            neighbour_dist = curr_dist + 1
            distances[neighbour] = neighbour_dist
            queue.append((neighbour, neighbour_dist))

    return len(
        {
            (pos, cheat)
            for pos in racetrack
            for cheat in get_cheats(pos)
            if cheat in racetrack and distances[cheat] - distances[pos] >= 102
        }
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
