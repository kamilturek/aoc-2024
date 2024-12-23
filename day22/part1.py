import sys


def mix(num1, num2):
    return num1 ^ num2


def prune(num):
    return num % 16777216


def generate_new_secret(secret, n=2000):
    for _ in range(n):
        secret = prune(mix(secret * 64, secret))
        secret = prune(mix(secret // 32, secret))
        secret = prune(mix(secret * 2048, secret))

    return secret


def solve(input):
    """
    >>> solve(open('input1.txt'))
    37327623
    >>> solve(open('input2.txt'))
    13004408787
    """
    return sum(generate_new_secret(secret) for secret in map(int, input))


if __name__ == "__main__":
    print(solve(sys.stdin))
