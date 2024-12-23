import time
import re

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]



som = 0
counter = 0
for line in lines:
    for x in re.finditer(r'mul\(([0-9]+),([0-9]+)\)', line):
        counter += 1
        start, end = x.span()
        print(line[start:end])

        som += int(x.groups()[0]) * int(x.groups()[1])

print(counter)
print(som)
print(time.time() - start_time)
