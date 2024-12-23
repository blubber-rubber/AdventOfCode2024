import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

A = int(lines[0].split(": ")[1])
B = int(lines[1].split(": ")[1])
C = int(lines[2].split(": ")[1])
REGISTERS = [A, B, C]
POINTER = 0
cache = [int(x) for x in lines[4].split(': ')[1].split(',')]


def get_combo_operand(n):
    if 0 <= n <= 3:
        return n

    elif 4 <= n <= 6:
        return REGISTERS[n - 4]


def adv(operand):
    REGISTERS[0] = int(REGISTERS[0] // (2 ** get_combo_operand(operand)))


def bxl(operand):
    REGISTERS[1] = REGISTERS[1] ^ operand


def bst(operand):
    REGISTERS[1] = get_combo_operand(operand) % 8


def jnz(operand):
    if REGISTERS[0] != 0:
        return operand


def bxc(operand):
    REGISTERS[1] = REGISTERS[1] ^ REGISTERS[2]


def out(operand):
    return get_combo_operand(operand) % 8


def bdv(operand):
    REGISTERS[1] = int(REGISTERS[0] // (2 ** get_combo_operand(operand)))


def cdv(operand):
    REGISTERS[2] = int(REGISTERS[0] // (2 ** get_combo_operand(operand)))


instructions = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}


def calculate_output_general(A):
    REGISTERS[0] = A
    REGISTERS[1] = 0
    REGISTERS[2] = 0
    POINTER = 0

    outputs = []
    while 0 <= POINTER < len(cache) - 1:
        opcode = cache[POINTER]
        operand = cache[POINTER + 1]
        result = instructions[opcode](operand)
        if opcode == 5:
            outputs.append(result)

        if opcode == 3 and result is not None:
            POINTER = result
        else:
            POINTER += 2

    return outputs



if __name__ == '__main__':
    print(','.join(str(x) for x in calculate_output_general(A)))

    print(time.time() - start_time)
