import time
from collections import defaultdict
from itertools import combinations

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

antennas = defaultdict(list)

n_rows = len(lines)
n_cols = len(lines[0])

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != '.':
            antennas[char].append((x, y))

antipodes = set()

for key, letter_ant in antennas.items():

    for a1, a2 in combinations(letter_ant, 2):
        dx = a2[0] - a1[0]
        dy = a2[1] - a1[1]

        ap1 = (a2[0] + dx, a2[1] + dy)
        ap2 = (a1[0] - dx, a1[1] - dy)

        if 0 <= ap1[0] < n_cols and 0 <= ap1[1] < n_rows:
            antipodes.add(ap1)

        if 0 <= ap2[0] < n_cols and 0 <= ap2[1] < n_rows:
            antipodes.add(ap2)

print(len(antipodes))
print(time.time() - start_time)
