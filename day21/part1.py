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
    126384
    >>> solve(open('input2.txt'))
    134120
    """
    num_sequences = compute_sequences(NUMERIC_KEYPAD)
    dir_sequences = compute_sequences(DIRECTIONAL_KEYPAD)

    total = 0

    for code in map(str.strip, input):
        num_seqs = [
            "".join(seq)
            for seq in itertools.product(
                *[num_sequences[(a, b)] for a, b in zip("A" + code, code)]
            )
        ]

        curr_seqs = num_seqs
        next_seqs = []

        for _ in range(2):
            for seq in curr_seqs:
                x = [dir_sequences[(a, b)] for a, b in zip("A" + seq, seq)]
                y = ["".join(s) for s in itertools.product(*x)]
                next_seqs.extend(y)

            curr_seqs = next_seqs
            next_seqs = []

        total += min(len(seq) for seq in curr_seqs) * int(code[:-1])

    return total


if __name__ == "__main__":
    print(solve(sys.stdin))
