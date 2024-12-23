import time
import re

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]





som = 0
counter = 0

line = ''.join(lines)
dos = [0]+[x.span()[0] for x in re.finditer(r'do\(\)', line)]
donts = [x.span()[0] for x in re.finditer(r"don't\(\)", line)]





for x in re.finditer(r'mul\(([0-9]+),([0-9]+)\)', line):
    counter += 1
    start, end = x.span()

    rel_do=[d for d in dos if d<start][-1]
    rel_donts = [d for d in donts if d < start]


    if not rel_donts or rel_do>rel_donts[-1]:
        som += int(x.groups()[0]) * int(x.groups()[1])


print(som)
print(time.time() - start_time)

