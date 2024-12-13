import math
import re
import sys

import numpy as np


def is_integer(number):
    return math.isclose(number, round(number))


def play(machine):
    button_a, button_b, prize = machine.splitlines()

    ax, ay = map(int, re.match(r"Button A: X\+(\d+), Y\+(\d+)", button_a).groups())
    bx, by = map(int, re.match(r"Button B: X\+(\d+), Y\+(\d+)", button_b).groups())
    px, py = map(int, re.match(r"Prize: X=(\d+), Y=(\d+)", prize).groups())

    A = np.array([[ax, bx], [ay, by]])
    B = np.array([px, py])

    count_a, count_b = np.linalg.solve(A, B)

    return (
        3 * round(count_a) + round(count_b)
        if is_integer(count_a) and is_integer(count_b)
        else 0
    )


def solve(input):
    """
    >>> solve(open('input1.txt'))
    480
    >>> solve(open('input2.txt'))
    34787
    """
    return sum(play(machine) for machine in input.read().split("\n\n"))


if __name__ == "__main__":
    print(solve(sys.stdin))
