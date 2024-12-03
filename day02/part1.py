import sys


def is_safe(levels):
    adjacent = list(zip(levels, levels[1:]))
    return (
        all(prev < curr for prev, curr in adjacent)
        or all(prev > curr for prev, curr in adjacent)
    ) and all(1 <= abs(prev - curr) <= 3 for prev, curr in adjacent)


def solve(input):
    """
    >>> solve(open('input1.txt'))
    2
    >>> solve(open('input2.txt'))
    236
    """
    return sum(
        1
        for levels in [[int(level) for level in line.split()] for line in input]
        if is_safe(levels)
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
