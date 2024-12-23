import sys
from collections import defaultdict


def solve(input):
    """
    >>> solve(open('input1.txt'))
    7
    >>> solve(open('input2.txt'))
    1314
    """
    connections = defaultdict(set)
    threes = set()

    for connection in input:
        computer1, computer2 = connection.strip().split("-")

        for computer3 in connections[computer1]:
            if computer2 in connections[computer3]:
                three = (computer1, computer2, computer3)
                if any(computer.startswith("t") for computer in three):
                    threes.add((computer1, computer2, computer3))

        connections[computer1].add(computer2)
        connections[computer2].add(computer1)

    return len(threes)


if __name__ == "__main__":
    print(solve(sys.stdin))
