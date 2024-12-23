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

        for i in range(1,min(dx, dy)):
            if dx % i == 0 and dy % i == 0:
                dx = dx // i
                dy = dy // i

        index = 0
        new_pos = a2

        while 0 <= new_pos[0] < n_cols and 0 <= new_pos[1] < n_rows:
            antipodes.add(new_pos)
            index += 1
            new_pos = (a2[0] + index * dx, a2[1] + index * dy)

        index = 0
        new_pos = a2

        while 0 <= new_pos[0] < n_cols and 0 <= new_pos[1] < n_rows:
            antipodes.add(new_pos)
            index -= 1
            new_pos = (a2[0] + index * dx, a2[1] + index * dy)


r = ''
for y in range(n_rows):
    for x in range(n_cols):
        if lines[y][x] == '.' and (x,y) in antipodes:
            r+= "#"
        else:
            r += lines[y][x]

    r+='\n'

print(r)
print(len(antipodes))
print(time.time() - start_time)
