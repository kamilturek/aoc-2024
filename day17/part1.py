import re
import sys


class Computer:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
        self.ptr = 0
        self.output = []

    def run(self, program):
        program = tuple(map(int, program.split(",")))

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


def solve(input):
    """
    >>> solve(open('input1.txt'))
    '0,1,2'
    >>> solve(open('input2.txt'))
    '4,2,5,6,7,7,7,7,3,1,0'
    >>> solve(open('input3.txt'))
    '4,6,3,5,6,3,5,2,1,0'
    >>> solve(open('input5.txt'))
    '1,3,7,4,6,4,2,3,5'
    """
    registers, program = input.read().split("\n\n")
    registers = map(int, re.findall(r"(\d+)", registers))
    program = program.split(":")[1].strip()

    computer = Computer(*registers)
    computer.run(program)

    return ",".join(map(str, computer.output))


if __name__ == "__main__":
    print(solve(sys.stdin))
