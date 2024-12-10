import sys

MOVES = (-1j, 1, 1j, -1)


def count_trails(pos, map_):
    curr_height = map_[pos]

    if curr_height == 9:
        return 1

    return sum(
        count_trails(pos + move, map_)
        for move in MOVES
        if map_.get(pos + move, -1) == curr_height + 1
    )


def solve(input):
    """
    >>> solve(open('input1.txt'))
    81
    >>> solve(open('input2.txt'))
    1609
    """
    map_ = {
        x + y * 1j: int(height)
        for y, row in enumerate(input.read().splitlines())
        for x, height in enumerate(row)
    }
    trailheads = (pos for pos, height in map_.items() if height == 0)

    return sum(count_trails(trailhead, map_) for trailhead in trailheads)


if __name__ == "__main__":
    print(solve(sys.stdin))
