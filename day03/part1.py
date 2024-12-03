import re
import sys


def solve(input):
    """
    >>> solve(open('input1.txt'))
    161
    >>> solve(open('input2.txt'))
    179571322
    """
    return sum(
        int(x) * int(y)
        for x, y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input.read())
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
