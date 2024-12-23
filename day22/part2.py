import sys
from collections import Counter, deque


def mix(num1, num2):
    return num1 ^ num2


def prune(num):
    return num % 16777216


def generate_new_secret(secret):
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(secret // 32, secret))
    secret = prune(mix(secret * 2048, secret))
    return secret


def get_buyer_prices(secret, n=2000):
    prices = {}
    changes = deque(maxlen=4)
    prev_price = int(str(secret)[-1])

    for _ in range(n):
        secret = generate_new_secret(secret)
        curr_price = int(str(secret)[-1])
        changes.append(curr_price - prev_price)

        sequence = tuple(changes)

        if len(sequence) >= 4 and sequence not in prices:
            prices[sequence] = curr_price

        prev_price = curr_price

    return prices


def solve(input):
    """
    >>> solve(open('input3.txt'))
    23
    >>> solve(open('input2.txt'))
    1455
    """
    prices = Counter()

    for secret in map(int, input):
        prices.update(get_buyer_prices(secret))

    return prices.most_common(n=1)[0][1]


if __name__ == "__main__":
    print(solve(sys.stdin))
