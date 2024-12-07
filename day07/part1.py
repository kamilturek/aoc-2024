import operator
import sys

OPERATORS = (
    operator.add,
    operator.mul,
)


def is_possible(value, numbers, target):
    if len(numbers) == 0:
        return value == target

    if value > target:
        return False

    return any(
        is_possible(operator(value, numbers[0]), numbers[1:], target)
        for operator in OPERATORS
    )


def parse_equations(input):
    for equation in input:
        target, numbers = equation.split(":")

        target = int(target)
        numbers = list(map(int, numbers.split()))

        yield target, numbers


def solve(input):
    """
    >>> solve(open('input1.txt'))
    3749
    >>> solve(open('input2.txt'))
    10741443549536
    """
    return sum(
        target
        for target, numbers in parse_equations(input)
        if is_possible(numbers[0], numbers[1:], target)
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
