import sys

MASK = (0, -1 - 1j, -1 + 1j, 1 - 1j, 1 + 1j)
PATTERNS = ("AMMSS", "ASSMM", "AMSMS", "ASMSM")


def solve(input):
    """
    >>> solve(open('input1.txt'))
    9
    >>> solve(open('input2.txt'))
    2000
    """
    matrix = {
        x + y * 1j: cell for x, row in enumerate(input) for y, cell in enumerate(row)
    }

    return sum(
        1
        for cell in matrix
        if "".join(matrix.get(cell + offset, ".") for offset in MASK) in PATTERNS
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
