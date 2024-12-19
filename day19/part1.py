import sys


def is_possible(design, patterns):
    return any(
        True
        if len(design[len(pattern) :]) == 0
        else is_possible(design[len(pattern) :], patterns)
        for pattern in patterns
        if design.startswith(pattern)
    )


def solve(input):
    """
    >>> solve(open('input1.txt'))
    6
    >>> solve(open('input2.txt'))
    233
    """
    patterns, designs = input.read().split("\n\n")
    patterns = tuple(patterns.split(", "))
    designs = designs.splitlines()

    return sum(is_possible(design, patterns) for design in designs)


if __name__ == "__main__":
    print(solve(sys.stdin))
