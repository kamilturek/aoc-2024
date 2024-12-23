import itertools
import re
import sys

WIDTH = 101
HEIGHT = 103
SECONDS = 100


def move(robots, seconds):
    return {
        ((px + vx * seconds) % WIDTH, (py + vy * seconds) % HEIGHT)
        for px, py, vx, vy in robots
    }


def has_long_line(row):
    return "X" * 20 in row


def solve(input):
    """
    >>> solve(open('input2.txt'))
    7687
    """
    robots = {
        tuple(map(int, re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", robot).groups()))
        for robot in input
    }

    for seconds in itertools.count():
        positions = move(robots, seconds)

        for y in range(HEIGHT):
            row = "".join(["X" if (x, y) in positions else " " for x in range(WIDTH)])
            if has_long_line(row):
                return seconds


if __name__ == "__main__":
    print(solve(sys.stdin))
