import itertools
import sys
from heapq import heappop, heappush

LEFT = -1
UP = -1j
RIGHT = 1
DOWN = 1j

MOVES = (LEFT, UP, RIGHT, DOWN)


def solve(input):
    """
    >>> solve(open('input1.txt'))
    7036
    >>> solve(open('input2.txt'))
    11048
    >>> solve(open('input3.txt'))
    143580
    """
    start, end = None, None
    maze = {}

    for y, row in enumerate(input.read().splitlines()):
        for x, node in enumerate(row):
            if node == "#":
                continue

            pos = x + y * 1j

            if node == "S":
                start = pos
            elif node == "E":
                end = pos

            maze[pos] = node

    distances = {pos: {direction: float("inf") for direction in MOVES} for pos in maze}
    distances[start][RIGHT] = 0

    counter = itertools.count()
    pq = [(0, next(counter), RIGHT, start)]
    visited = set()

    while pq:
        curr_distance, _, curr_direction, curr_pos = heappop(pq)

        if (curr_pos, curr_direction) in visited:
            continue

        visited.add((curr_pos, curr_direction))

        neighbour = curr_pos + curr_direction
        if neighbour in maze:
            distance = curr_distance + 1
            if distance < distances[neighbour][curr_direction]:
                distances[neighbour][curr_direction] = distance
                heappush(pq, (distance, next(counter), curr_direction, neighbour))

        for new_direction in MOVES:
            if new_direction == curr_direction:
                continue

            distance = curr_distance + 1000
            if distance < distances[curr_pos][new_direction]:
                distances[curr_pos][new_direction] = distance
                heappush(pq, (distance, next(counter), new_direction, curr_pos))

    return min(distances[end].values())


if __name__ == "__main__":
    print(solve(sys.stdin))
