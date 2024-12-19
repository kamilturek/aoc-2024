import sys
from dataclasses import astuple, dataclass, field
from heapq import heappop, heappush

LEFT = -1
UP = -1j
RIGHT = 1
DOWN = 1j

MOVES = (LEFT, UP, RIGHT, DOWN)

WIDTH = 70
HEIGHT = 70


@dataclass(order=True)
class Node:
    dist: int
    pos: complex = field(compare=False)


def neighbours(pos):
    return (pos + move for move in MOVES)


def in_bounds(pos):
    return 0 <= int(pos.real) <= WIDTH and 0 <= int(pos.imag) <= HEIGHT


def can_reach_end(start, end, corrupted):
    pq = [Node(dist=0, pos=start)]
    distances = {start: 0}
    visited = set()

    while len(pq) > 0:
        curr_dist, curr_pos = astuple(heappop(pq))

        if curr_pos in visited:
            continue

        visited.add(curr_pos)

        for neighbour in neighbours(curr_pos):
            if not in_bounds(neighbour) or neighbour in corrupted:
                continue

            neighbour_dist = curr_dist + 1

            if neighbour not in distances or neighbour_dist < distances[neighbour]:
                distances[neighbour] = neighbour_dist
                heappush(pq, Node(dist=neighbour_dist, pos=neighbour))

    return end in distances


def solve(input):
    """
    >>> solve(open('input2.txt'))
    '64,54'
    """
    start = 0 + 0j
    end = WIDTH + HEIGHT * 1j
    corrupted = set()

    for coords in input:
        x, y = map(int, coords.split(","))
        corrupted.add(x + y * 1j)

        if not can_reach_end(start, end, corrupted):
            return f"{x},{y}"


if __name__ == "__main__":
    print(solve(sys.stdin))
