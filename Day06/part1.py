import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]



n_rows = len(lines)
n_cols = len(lines[0])

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

positions = set()

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '^':
            current_pos = (x, y)
            positions.add((x, y))


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

    current_pos=new_pos

print(len(positions))
print(time.time() - start_time)
