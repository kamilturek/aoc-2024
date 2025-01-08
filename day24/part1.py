import operator
import re
import sys

OPERATORS = {
    "AND": operator.and_,
    "OR": operator.or_,
    "XOR": operator.xor,
}


def eval(wire, wires):
    x = wires[wire]
    if isinstance(x, tuple):
        in1, op, in2 = x
        in1 = eval(in1, wires)
        in2 = eval(in2, wires)
        return op(in1, in2)
    return x


def solve(input):
    """
    >>> solve(open('input1.txt'))
    4
    >>> solve(open('input2.txt'))
    2024
    >>> solve(open('input3.txt'))
    51410244478064
    """
    wires = {}
    zlen = 0

    values, gates = input.read().split("\n\n")
    for init in values.splitlines():
        gate, value = re.match(r"(\w\d+): (\d+)", init).groups()
        wires[gate] = int(value)

    for gate in gates.splitlines():
        in1, op, in2, out = re.match(
            r"([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)", gate
        ).groups()
        wires[out] = (in1, OPERATORS[op], in2)

        if out.startswith("z"):
            zlen = max(zlen, int(out[1:]) + 1)

    output = 0
    for z in reversed(range(zlen)):
        wire = f"z{z:0>2}"
        output = output << 1
        output |= eval(wire, wires)

    return output


if __name__ == "__main__":
    print(solve(sys.stdin))
