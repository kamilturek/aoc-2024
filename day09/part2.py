import itertools
import sys

FREE = "."


def solve(input):
    """
    >>> solve(open('input1.txt'))
    2858
    >>> solve(open('input2.txt'))
    6363268339304
    """
    disk = []
    file_blocks = []
    free_blocks = []

    for file_id, block in enumerate(itertools.batched(input.read().strip(), 2)):
        file_len = int(block[0])
        free_len = int(block[1]) if len(block) == 2 else 0

        file_start = len(disk)
        disk.extend([file_id] * int(file_len))
        disk.extend([FREE] * int(free_len))
        file_blocks.append((file_id, file_start, file_len))
        free_blocks.append((file_start + file_len, free_len))

    for file_id, file_start, file_len in reversed(file_blocks):
        for i, (free_start, free_len) in enumerate(free_blocks):
            if free_start >= file_start:
                break

            if free_len >= file_len:
                disk[file_start : file_start + file_len] = [FREE] * file_len
                disk[free_start : free_start + file_len] = [file_id] * file_len
                free_blocks[i] = (free_start + file_len, free_len - file_len)
                break

    return sum(
        block_idx * int(block) for block_idx, block in enumerate(disk) if block != FREE
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
