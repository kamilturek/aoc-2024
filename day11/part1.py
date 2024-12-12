import sys

BLINKS = 25


def transform(stone):
    if stone == 0:
        return [1]

    digits = str(stone)
    if len(digits) % 2 == 0:
        return [int(digits[: len(digits) // 2]), int(digits[len(digits) // 2 :])]

    return [stone * 2024]


def solve(input):
    """
    >>> solve(open('input1.txt'))
    55312
    >>> solve(open('input2.txt'))
    198089
    """
    stones = list(map(int, input.read().split()))

    for _ in range(BLINKS):
        stones = [new for stone in stones for new in transform(stone)]

    return len(stones)


if __name__ == "__main__":
    print(solve(sys.stdin))
