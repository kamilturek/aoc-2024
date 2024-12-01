import sys


def solve(input):
    """
    >>> solve(open('input1.txt'))
    11
    >>> solve(open('input2.txt'))
    1834060
    """
    left, right = zip(*[map(int, line.split()) for line in input])
    return sum(abs(lnum - rnum) for lnum, rnum in zip(sorted(left), sorted(right)))


if __name__ == "__main__":
    print(solve(sys.stdin))
