import time
import re

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

split_index = lines.index('')
registers = {}

for line in lines[:split_index]:
    name, val = line.split(': ')
    registers[name] = int(val)

instructions = []
for line in lines[split_index + 1:]:
    instructions.append(line)

done = set()


def f_xor(a, b):
    return registers[a] ^ registers[b]


def f_or(a, b):
    return int(registers[a] or registers[b])


def f_and(a, b):
    return int(registers[a] and registers[b])


functions = {'AND': f_and, 'OR': f_or, 'XOR': f_xor}

while set(instructions).difference(done):
    instr_list = [i for i in instructions if i not in done]
    for instr in instr_list:
        n1, f, n2, n3 = re.match('([^ ]*) (XOR|AND|OR) ([^ ]*) -> ([^ ]*)', instr).groups()

        if n1 in registers and n2 in registers:
            registers[n3] = functions[f](n1, n2)
            done.add(instr)
            print(n1, n2, n3, f)
    print('-----')

keys = [r for r in registers.keys() if r.startswith('z')]

outputs = []

for key in sorted(keys):
    print(key, registers[key])
    outputs.append(str(registers[key]))

print(outputs)
print(int(''.join(reversed(outputs)), 2))

print(time.time() - start_time)
