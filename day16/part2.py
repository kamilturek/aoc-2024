import itertools
import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

LEFT = -1
UP = -1j
RIGHT = 1
DOWN = 1j

MOVES = (LEFT, UP, RIGHT, DOWN)


def get_path(pos, predecessors):
    path = set([pos])
    seen = set()
    q = deque([(pos, UP)])

    while q:
        pos, dir = q.pop()
        for pred, dir in predecessors[pos][dir]:
            if (pred, dir) not in seen:
                path.add(pred)
                seen.add((pred, dir))
                q.appendleft((pred, dir))

    return path


def solve(input):
    """
    >>> solve(open('input1.txt'))
    45
    >>> solve(open('input2.txt'))
    64
    >>> solve(open('input3.txt'))
    645
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
    predecessors = defaultdict(lambda: defaultdict(list))

    while pq:
        curr_distance, _, curr_direction, curr_pos = heappop(pq)

        if (curr_pos, curr_direction) in visited:
            continue

        visited.add((curr_pos, curr_direction))

        neighbour = curr_pos + curr_direction
        if neighbour in maze:
            new_distance = curr_distance + 1

            if new_distance < distances[neighbour][curr_direction]:
                distances[neighbour][curr_direction] = new_distance
                predecessors[neighbour][curr_direction] = [(curr_pos, curr_direction)]
                heappush(pq, (new_distance, next(counter), curr_direction, neighbour))
            elif new_distance == distances[neighbour][curr_direction]:
                predecessors[neighbour][curr_direction].append(
                    (curr_pos, curr_direction)
                )

        for new_direction in MOVES:
            if new_direction == curr_direction:
                continue

            new_distance = curr_distance + 1000

            if new_distance < distances[curr_pos][new_direction]:
                distances[curr_pos][new_direction] = new_distance
                heappush(pq, (new_distance, next(counter), new_direction, curr_pos))
                predecessors[curr_pos][new_direction] = [(curr_pos, curr_direction)]
            elif new_distance == distances[curr_pos][new_direction]:
                predecessors[curr_pos][new_direction].append((curr_pos, curr_direction))

    return len(get_path(end, predecessors))


if __name__ == "__main__":
    print(solve(sys.stdin))
