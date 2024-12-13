import sys

LEFT = -1
RIGHT = 1
UP = -1j
DOWN = 1j

MOVES = (LEFT, RIGHT, UP, DOWN)


def neighbours(pos):
    yield from (pos + move for move in MOVES)


def is_outer_corner(pos, garden):
    plant = garden.get(pos)
    corners = (
        (pos + LEFT, pos + UP),
        (pos + LEFT, pos + DOWN),
        (pos + RIGHT, pos + UP),
        (pos + RIGHT, pos + DOWN),
    )

    return sum(
        1
        for corner in corners
        if all(plant != garden.get(neighbour) for neighbour in corner)
    )


def is_inner_corner(pos, garden):
    plant = garden.get(pos)
    corners = [
        (pos + LEFT, pos + UP, pos + LEFT + UP),
        (pos + LEFT, pos + DOWN, pos + LEFT + DOWN),
        (pos + RIGHT, pos + UP, pos + RIGHT + UP),
        (pos + RIGHT, pos + DOWN, pos + RIGHT + DOWN),
    ]

    return sum(
        1
        for corner in corners
        if plant
        == garden.get(corner[0])
        == garden.get(corner[1])
        != garden.get(corner[2])
    )


def solve(input):
    """
    >>> solve(open('input1.txt'))
    80
    >>> solve(open('input2.txt'))
    436
    >>> solve(open('input3.txt'))
    1206
    >>> solve(open('input4.txt'))
    236
    >>> solve(open('input5.txt'))
    851994
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
        corners = 0
        region = {pos}

        while len(region) > 0:
            curr = region.pop()

            visited.add(curr)
            area += 1

            corners += is_outer_corner(curr, garden) + is_inner_corner(curr, garden)

            for neighbour in neighbours(curr):
                if garden.get(neighbour) == plant and neighbour not in visited:
                    region.add(neighbour)

        price += area * corners

    return price


if __name__ == "__main__":
    print(solve(sys.stdin))
