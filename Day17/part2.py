import time
from part1 import calculate_output_general

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

CACHE = [int(x) for x in lines[4].split(': ')[1].split(',')]
OPL = []


def decimal2bin(x):
    return f'{bin(x)[2:]:>03}'


def calculate_output(A):
    outputs = []
    while A != 0:
        B = (((A % 8) ^ 1) ^ (A >> ((A % 8) ^ 1))) ^ 6
        A = A >> 3

        outputs.append(B % 8)

    return outputs


def dfs(current_lijst):
    if len(current_lijst) == len(CACHE) +1:
        A = int(''.join(decimal2bin(i) for i in current_lijst), 2)

        OPL.append(A)
        return

    for x in range(8):
        current_lijst.append(x)
        A = int(''.join(decimal2bin(i) for i in current_lijst), 2)

        #output = calculate_output(A)
        output = calculate_output_general(A)
        if len(output) + 1 == len(current_lijst):
            if all(x == y for x, y in zip(CACHE[-len(output):], output)):
                dfs(current_lijst)

        del current_lijst[-1]


current_lijst = [0]
dfs(current_lijst)

# print(min(OPL))
for opl in sorted(OPL):
    print(opl, calculate_output(opl))




print(time.time() - start_time)
