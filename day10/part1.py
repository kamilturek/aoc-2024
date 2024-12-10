import sys

MOVES = (-1j, 1, 1j, -1)


def count_peaks(trailhead, map_):
    trails = [trailhead]
    peaks = set()

    while len(trails) > 0:
        curr_pos = trails.pop()
        curr_height = map_[curr_pos]

        if curr_height == 9:
            peaks.add(curr_pos)
            continue

        trails.extend(
            [
                curr_pos + move
                for move in MOVES
                if map_.get(curr_pos + move, -1) == curr_height + 1
            ]
        )

    return len(peaks)


def solve(input):
    """
    >>> solve(open('input1.txt'))
    36
    >>> solve(open('input2.txt'))
    754
    """
    map_ = {
        x + y * 1j: int(height)
        for y, row in enumerate(input.read().splitlines())
        for x, height in enumerate(row)
    }
    trailheads = (pos for pos, height in map_.items() if height == 0)

    return sum(count_peaks(trailhead, map_) for trailhead in trailheads)


if __name__ == "__main__":
    print(solve(sys.stdin))
