import itertools
import sys

FREE = "."


def solve(input):
    """
    >>> solve(open('input1.txt'))
    1928
    >>> solve(open('input2.txt'))
    6331212425418
    """
    disk = []

    for file_id, blocks in enumerate(itertools.batched(input.read().strip(), 2)):
        file_len = int(blocks[0])
        free_len = int(blocks[1]) if len(blocks) == 2 else 0

        disk.extend([file_id] * file_len)
        disk.extend(["."] * free_len)

    free_blocks = (block_idx for block_idx, block in enumerate(disk) if block == FREE)

    for block_idx in reversed(range(len(disk))):
        if disk[block_idx] == FREE:
            continue

        free_block_idx = next(free_blocks, None)
        if free_block_idx is None or free_block_idx >= block_idx:
            break

        disk[free_block_idx] = disk[block_idx]
        disk[block_idx] = FREE

    return sum(
        block_idx * int(block) for block_idx, block in enumerate(disk) if block != FREE
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
