import itertools
import sys
from collections import defaultdict


def is_complete_graph(computers, connections):
    for computer in computers:
        if len(connections[computer]) < (len(computers) - 1):
            return False

        for another_computer in computers:
            if computer == another_computer:
                continue

            if computer not in connections[another_computer]:
                return False

    return True


def find_largest_lan_party(computers, connections):
    return next(
        combination
        for r in reversed(range(len(computers) + 1))
        for combination in itertools.combinations(computers, r)
        if is_complete_graph(combination, connections)
    )


def solve(input):
    """
    >>> solve(open('input1.txt'))
    'co,de,ka,ta'
    >>> solve(open('input2.txt'))
    'bg,bu,ce,ga,hw,jw,nf,nt,ox,tj,uu,vk,wp'
    """
    connections = defaultdict(set)
    largest_lan_party = set()

    for connection in input:
        computer1, computer2 = connection.strip().split("-")
        connections[computer1].add(computer2)
        connections[computer2].add(computer1)

        lan_party = find_largest_lan_party(
            computers={computer1, *connections[computer1]},
            connections=connections,
        )

        if len(lan_party) > len(largest_lan_party):
            largest_lan_party = lan_party

    return ",".join(sorted(largest_lan_party))


if __name__ == "__main__":
    print(solve(sys.stdin))
