import itertools
import sys
from collections import defaultdict


def solve(input):
    """
    >>> solve(open('input1.txt'))
    14
    >>> solve(open('input2.txt'))
    396
    """
    matrix = input.read().splitlines()
    rows = len(matrix)
    cols = len(matrix[0])

    frequencies = defaultdict(list)

    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            if cell != ".":
                frequencies[cell].append(x + y * 1j)

    antinodes = set()

    for antennas in frequencies.values():
        for antenna1, antenna2 in itertools.combinations(antennas, 2):
            dist = antenna1 - antenna2

            for antinode in [antenna1 + dist, antenna2 - dist]:
                if 0 <= int(antinode.real) < cols and 0 <= int(antinode.imag) < rows:
                    antinodes.add(antinode)

    return len(antinodes)


if __name__ == "__main__":
    print(solve(sys.stdin))
