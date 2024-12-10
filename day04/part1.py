import sys

MASKS = (
    # Horizontally Right
    (0, 1, 2, 3),
    # Horizontally Left
    (0, -1, -2, -3),
    # Vertically Up
    (0, -1j, -2j, -3j),
    # Vertically Down
    (0, 1j, 2j, 3j),
    # Diagonally Right Up
    (0, 1 - 1j, 2 - 2j, 3 - 3j),
    # Diagonally Right Down
    (0, 1 + 1j, 2 + 2j, 3 + 3j),
    # Diagonally Left Up
    (0, -1 - 1j, -2 - 2j, -3 - 3j),
    # Diagonally Left Down
    (0, -1 + 1j, -2 + 2j, -3 + 3j),
)


def solve(input):
    """
    >>> solve(open('input1.txt'))
    18
    >>> solve(open('input2.txt'))
    2646
    """
    matrix = {
        x + y * 1j: cell for y, row in enumerate(input) for x, cell in enumerate(row)
    }

    return sum(
        1
        for cell in matrix
        for mask in MASKS
        if "".join(matrix.get(cell + offset, ".") for offset in mask) == "XMAS"
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
