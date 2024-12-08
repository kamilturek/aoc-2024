import itertools
import sys
from collections import defaultdict


def solve(input):
    """
    >>> solve(open('input1.txt'))
    34
    >>> solve(open('input2.txt'))
    1200
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

            while 0 <= int(antenna1.real) < cols and 0 <= int(antenna1.imag) < rows:
                antinodes.add(antenna1)
                antenna1 += dist

            while 0 <= int(antenna2.real) < cols and 0 <= int(antenna2.imag) < rows:
                antinodes.add(antenna2)
                antenna2 -= dist

    return len(antinodes)


if __name__ == "__main__":
    print(solve(sys.stdin))
