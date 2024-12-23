import time
from collections import defaultdict

start_time = time.time()

with open('input.txt') as f:
    lines = [[c for c in line.rstrip('\n')] for line in f.readlines()]

n_rows = len(lines)
n_cols = len(lines[0])

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

positions = set()

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '^':
            start_pos = (x, y)
            current_pos = (x, y)
            positions.add(current_pos)


def is_inbound(pos, n_rows, n_cols):
    return 0 <= pos[0] < n_cols and 0 <= pos[1] < n_rows


dir_index = 0
inbounds = True
while is_inbound(current_pos, n_rows, n_cols):
    new_pos = (current_pos[0] + dirs[dir_index][0], current_pos[1] + dirs[dir_index][1])

    while is_inbound(new_pos, n_rows, n_cols) and lines[new_pos[1]][new_pos[0]] == '#':
        dir_index = (dir_index + 1) % 4
        new_pos = (current_pos[0] + dirs[dir_index][0], current_pos[1] + dirs[dir_index][1])

    if is_inbound(new_pos, n_rows, n_cols):
        positions.add(new_pos)
    current_pos = new_pos

count = 0

for pos in positions:
    place = lines[pos[1]][pos[0]]
    if place not in ('^', '#'):
        lines[pos[1]][pos[0]] = '#'

        positions2 = defaultdict(list)
        current_pos = start_pos

        dir_index = 0
        while is_inbound(current_pos, n_rows, n_cols) and dir_index not in positions2[current_pos]:
            positions2[current_pos].append(dir_index)
            new_pos = (current_pos[0] + dirs[dir_index][0], current_pos[1] + dirs[dir_index][1])

            while is_inbound(new_pos, n_rows, n_cols) and lines[new_pos[1]][new_pos[0]] == '#':
                dir_index = (dir_index + 1) % 4
                new_pos = (current_pos[0] + dirs[dir_index][0], current_pos[1] + dirs[dir_index][1])

            current_pos = new_pos

        if is_inbound(current_pos, n_rows, n_cols):
            count += 1

        lines[pos[1]][pos[0]] = '.'

print(count)
print(time.time() - start_time)
