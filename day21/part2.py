import functools
import itertools
import sys
from collections import deque

NUMERIC_KEYPAD = {
    (0 + 0j): "7",
    (1 + 0j): "8",
    (2 + 0j): "9",
    (0 + 1j): "4",
    (1 + 1j): "5",
    (2 + 1j): "6",
    (0 + 2j): "1",
    (1 + 2j): "2",
    (2 + 2j): "3",
    (1 + 3j): "0",
    (2 + 3j): "A",
}

DIRECTIONAL_KEYPAD = {
    (1 + 0j): "^",
    (2 + 0j): "A",
    (0 + 1j): "<",
    (1 + 1j): "v",
    (2 + 1j): ">",
}


def compute_sequences(keypad):
    sequences = {}

    for start in keypad:
        for end in keypad:
            if start == end:
                sequences[(keypad[start], keypad[end])] = ["A"]
                continue

            possibilities = []

            q = deque([(start, "")])
            optimal = float("inf")

            while len(q) > 0:
                curr_pos, curr_seq = q.popleft()

                for diff, move in ((-1, "<"), (1, ">"), (-1j, "^"), (1j, "v")):
                    next_pos = curr_pos + diff

                    if next_pos not in keypad:
                        continue

                    next_seq = curr_seq + move

                    if len(next_seq) > optimal:
                        break

                    if next_pos == end and len(next_seq) <= optimal:
                        optimal = len(next_seq)
                        possibilities.append(next_seq + "A")
                        continue

                    q.append((next_pos, next_seq))

            sequences[(keypad[start], keypad[end])] = possibilities

    return sequences


def solve(input):
    """
    >>> solve(open('input1.txt'))
    154115708116294
    >>> solve(open('input2.txt'))
    167389793580400
    """
    num_sequences = compute_sequences(NUMERIC_KEYPAD)
    dir_sequences = compute_sequences(DIRECTIONAL_KEYPAD)

    @functools.cache
    def compute_length(a, b, depth):
        if depth == 1:
            return min(len(s) for s in dir_sequences[(a, b)])

        optimal = float("inf")
        for seq in dir_sequences[(a, b)]:
            length = 0
            for x, y in zip("A" + seq, seq):
                length += compute_length(x, y, depth - 1)
            optimal = min(optimal, length)
        return optimal

    total = 0

    for code in map(str.strip, input):
        num_seqs = [
            "".join(seq)
            for seq in itertools.product(
                *[num_sequences[(a, b)] for a, b in zip("A" + code, code)]
            )
        ]

        curr_seqs = num_seqs

        optimal = float("inf")
        for seq in curr_seqs:
            length = 0
            for a, b in zip("A" + seq, seq):
                length += compute_length(a, b, depth=25)
            optimal = min(optimal, length)

        total += optimal * int(code[:-1])

    return total


if __name__ == "__main__":
    print(solve(sys.stdin))
