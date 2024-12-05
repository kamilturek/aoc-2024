import sys
from collections import defaultdict


def is_ordered(page, ordering):
    seen = set()

    for num in page:
        for before in ordering[num]:
            if before in seen:
                return False

        seen.add(num)

    return True


def solve(input):
    """
    >>> solve(open('input1.txt'))
    143
    >>> solve(open('input2.txt'))
    5208
    """
    raw_ordering, raw_pages = [
        part.split("\n") for part in input.read().strip().split("\n\n")
    ]

    ordering = defaultdict(list)
    for order in raw_ordering:
        before, after = order.split("|")
        ordering[int(before)].append(int(after))

    pages = [[int(num) for num in page.split(",")] for page in raw_pages]

    return sum(page[len(page) // 2] for page in pages if is_ordered(page, ordering))


if __name__ == "__main__":
    print(solve(sys.stdin))
