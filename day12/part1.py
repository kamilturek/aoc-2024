import sys

LEFT = -1
RIGHT = 1
UP = -1j
DOWN = 1j

MOVES = (LEFT, RIGHT, UP, DOWN)


def neighbours(pos):
    yield from (pos + move for move in MOVES)


def solve(input):
    """
    >>> solve(open('input1.txt'))
    140
    >>> solve(open('input2.txt'))
    772
    >>> solve(open('input3.txt'))
    1930
    >>> solve(open('input5.txt'))
    1400386
    """
    garden = {
        x + y * 1j: plant
        for y, row in enumerate(input.read().splitlines())
        for x, plant in enumerate(row)
    }

    price = 0
    visited = set()

    for pos, plant in garden.items():
        if pos in visited:
            continue

        area = 0
        perimeter = 0
        region = {pos}

        while len(region) > 0:
            curr_pos = region.pop()

            visited.add(curr_pos)
            area += 1

            for neighbour in neighbours(curr_pos):
                if garden.get(neighbour) != plant:
                    perimeter += 1
                elif neighbour not in visited:
                    region.add(neighbour)

        price += area * perimeter

    return price


if __name__ == "__main__":
    print(solve(sys.stdin))
