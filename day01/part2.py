import sys
from collections import Counter


def solve(input):
    """
    >>> solve(open('input1.txt'))
    31
    >>> solve(open('input2.txt'))
    21607792
    """
    left, right = zip(*[map(int, line.split()) for line in input])
    right_counter = Counter(right)

    return sum(lnum * right_counter[lnum] for lnum in left)


if __name__ == "__main__":
    print(solve(sys.stdin))
