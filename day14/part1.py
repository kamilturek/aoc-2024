import functools
import operator
import re
import sys

WIDTH = 101
HEIGHT = 103
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

SECONDS = 100


def solve(input):
    """
    >>> solve(open('input2.txt'))
    214109808
    """
    robots = set()
    quadrants = [0] * 4

    for robot in input:
        px, py, vx, vy = map(
            int, re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", robot).groups()
        )

        px = (px + vx * SECONDS) % WIDTH
        py = (py + vy * SECONDS) % HEIGHT

        if px < HALF_WIDTH:
            if py < HALF_HEIGHT:
                quadrants[0] += 1
            elif HALF_HEIGHT < py:
                quadrants[1] += 1
        elif px > HALF_WIDTH:
            if py < HALF_HEIGHT:
                quadrants[2] += 1
            elif HALF_HEIGHT < py:
                quadrants[3] += 1

        robots.add((px, py))

    return functools.reduce(operator.mul, quadrants, 1)


if __name__ == "__main__":
    print(solve(sys.stdin))
