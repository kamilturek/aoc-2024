import sys
from collections import Counter

BLINKS = 75


def transform(stone):
    if stone == 0:
        return [1]

    digits = str(stone)
    if len(digits) % 2 == 0:
        return [int(digits[: len(digits) // 2]), int(digits[len(digits) // 2 :])]

    return [stone * 2024]


def solve(input):
    """
    >>> solve(open('input2.txt'))
    236302670835517
    """
    stones = Counter(map(int, input.read().split()))

    for _ in range(BLINKS):
        new_stones = Counter()

        for stone, count in stones.items():
            for new_stone in transform(stone):
                new_stones[new_stone] += count

        stones = new_stones

    return stones.total()


if __name__ == "__main__":
    print(solve(sys.stdin))
