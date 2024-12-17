import sys


class Computer:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
        self.ptr = 0
        self.output = []

    def run(self, program):
        while self.ptr < len(program):
            opcode = program[self.ptr]
            operand = program[self.ptr + 1]

            self.ptr += 2

            instruction = self.get_instruction(opcode)
            instruction(operand)

    def get_instruction(self, opcode):
        match opcode:
            case 0:
                return self.adv
            case 1:
                return self.bxl
            case 2:
                return self.bst
            case 3:
                return self.jnz
            case 4:
                return self.bxc
            case 5:
                return self.out
            case 6:
                return self.bdv
            case 7:
                return self.cdv

        raise ValueError("Unknown opcode")

    def get_combo_operand(self, operand):
        return (0, 1, 2, 3, self.a, self.b, self.c)[operand]

    def adv(self, operand):
        self.a = self.a >> self.get_combo_operand(operand)

    def bxl(self, operand):
        self.b = self.b ^ operand

    def bst(self, operand):
        self.b = self.get_combo_operand(operand) & 0b111

    def jnz(self, operand):
        if self.a == 0:
            return

        self.ptr = operand

    def bxc(self, operand):
        self.b = self.b ^ self.c

    def out(self, operand):
        self.output.append(self.get_combo_operand(operand) & 0b111)

    def bdv(self, operand):
        self.b = self.a >> self.get_combo_operand(operand)

    def cdv(self, operand):
        self.c = self.a >> self.get_combo_operand(operand)


def find_a(a, output, program):
    """
    Find register A value producing the given output
    by processing the given program.
    """

    computer = Computer(a=a, b=0, c=0)
    computer.run(program)

    candidates = []

    if computer.output[0] == output[-1]:
        if len(output) == 1:
            return [a]

        for digit in range(8):
            next_a = (a << 3) | digit
            candidates.extend(find_a(next_a, output[:-1], program))

    return candidates


def solve(input):
    """
    >>> solve(open('input4.txt'))
    117440
    >>> solve(open('input5.txt'))
    202367025818154
    """
    _, program = input.read().split("\n\n")
    program = tuple(map(int, program.split(":")[1].strip().split(",")))

    return min(
        a
        for digit in range(8)
        for a in find_a(a=digit, output=program, program=program)
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
