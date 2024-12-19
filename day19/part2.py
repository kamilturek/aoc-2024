import functools
import sys


@functools.cache
def count_options(design, patterns):
    return sum(
        1
        if len(design[len(pattern) :]) == 0
        else count_options(design[len(pattern) :], patterns)
        for pattern in patterns
        if design.startswith(pattern)
    )


def solve(input):
    """
    >>> solve(open('input1.txt'))
    16
    >>> solve(open('input2.txt'))
    691316989225259
    """
    patterns, designs = input.read().split("\n\n")
    patterns = tuple(patterns.split(", "))
    designs = designs.splitlines()

    return sum(count_options(design, patterns) for design in designs)


if __name__ == "__main__":
    print(solve(sys.stdin))
