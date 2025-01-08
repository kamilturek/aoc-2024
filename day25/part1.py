import sys

MAX_HEIGHT = 6


def count_lock_heights(rows):
    heights = [0] * len(rows[0])

    for row in rows[1:]:
        for i, col in enumerate(row):
            if col == "#":
                heights[i] += 1

    return heights


def count_key_heights(rows):
    heights = [MAX_HEIGHT - 1] * len(rows[0])

    for row in rows[1:]:
        for i, col in enumerate(row):
            if col == ".":
                heights[i] -= 1

    return heights


def solve(input):
    """
    >>> solve(open('input1.txt'))
    3
    >>> solve(open('input2.txt'))
    3107
    """
    schematics = map(str.strip, input.read().split("\n\n"))
    locks = []
    keys = []

    for schematic in schematics:
        rows = schematic.splitlines()
        is_lock = all(cell == "#" for cell in rows[0])

        if is_lock:
            locks.append(count_lock_heights(rows))
        else:
            keys.append(count_key_heights(rows))

    count = 0

    for lock in locks:
        for key in keys:
            for lh, kh in zip(lock, key):
                if lh + kh >= MAX_HEIGHT:
                    break
            else:
                count += 1

    return count


if __name__ == "__main__":
    print(solve(sys.stdin))
