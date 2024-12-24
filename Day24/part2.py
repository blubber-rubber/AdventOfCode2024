import time
import re

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

split_index = lines.index('')

instructions = {}
for line in lines[split_index + 1:]:
    a, f, b, r = re.match('([^ ]*) (XOR|AND|OR) ([^ ]*) -> ([^ ]*)', line).groups()

    instructions[(a, f, b)] = r

bit = 0
carry = None


def get_output_node(n1, f, n2):
    if (n1, f, n2) in instructions:
        return instructions[(n1, f, n2)]
    else:
        return instructions[(n2, f, n1)]


def get_inst(o):
    for key in instructions.keys():
        if instructions[key] == o:
            return key


switches = []

sk1 = ('scp', 'XOR', 'vkd')
sv1 = get_output_node(*sk1)
sv2 = 'z06'
sk2 = get_inst(sv2)

instructions[sk1] = sv2
instructions[sk2] = sv1

switches += [sv1, sv2]

##############
sk1 = ('rmd', 'XOR', 'nmm')
sv1 = get_output_node(*sk1)
sv2 = 'z11'
sk2 = get_inst(sv2)

instructions[sk1] = sv2
instructions[sk2] = sv1
switches += [sv1, sv2]

##############
sk1 = ('x23', 'XOR', 'y23')
sv1 = get_output_node(*sk1)
sv2 = 'ggt'
sk2 = get_inst(sv2)

instructions[sk1] = sv2
instructions[sk2] = sv1
switches += [sv1, sv2]

##############
sk1 = ('kwj', 'XOR', 'bhv')
sv1 = get_output_node(*sk1)
sv2 = 'z35'
sk2 = get_inst(sv2)

instructions[sk1] = sv2
instructions[sk2] = sv1
switches += [sv1, sv2]

while bit < 45:
    x_bit = f'x{bit:>02}'
    y_bit = f'y{bit:>02}'
    z_bit = f'z{bit:>02}'

    r1 = get_output_node(x_bit, 'XOR', y_bit)
    c1 = get_output_node(x_bit, 'AND', y_bit)

    if carry is None:
        carry = c1
        assert r1 == z_bit



    else:
        r2 = get_output_node(carry, 'XOR', r1)
        c2 = get_output_node(r1, 'AND', carry)
        carry = get_output_node(c2, 'OR', c1)
        assert r2 == z_bit

    bit += 1

switches.sort()
print(','.join(switches))
print(time.time() - start_time)
