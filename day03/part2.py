import re
import sys


def scan_memory(memory):
    enabled = True

    for x, y, do, dont in re.findall(
        r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", memory
    ):
        if do:
            enabled = True
            continue

        if dont:
            enabled = False
            continue

        if enabled:
            yield int(x) * int(y)


def solve(input):
    """
    >>> solve(open('input3.txt'))
    48
    >>> solve(open('input2.txt'))
    103811193
    """
    return sum(scan_memory(input.read()))


if __name__ == "__main__":
    print(solve(sys.stdin))
