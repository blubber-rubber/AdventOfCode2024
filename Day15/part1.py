import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

split_index = lines.index('')

grid = [[c for c in line] for line in lines[:split_index]]

instructions = ''.join(lines[split_index:])

dirs = {'^': (0, -1), '>': (1, 0), '<': (-1, 0), 'v': (0, 1)}

N_ROWS = len(grid)
N_COLS = len(grid[0])
current_pos = [(x, y) for x in range(N_COLS) for y in range(N_ROWS) if grid[y][x] == '@'][0]

for instr in instructions:

    dx, dy = dirs[instr]

    pushed = {}
    push = [current_pos]

    while push:
        px, py = push.pop(0)
        if (px, py) not in pushed:
            pushed[(px, py)] = grid[py][px]

            if grid[py][px] in "O@":
                nx, ny = px + dx, py + dy
                push.append((nx, ny))

    if '#' not in pushed.values():
        for kx, ky in pushed.keys():
            if (kx - dx, ky - dy) in pushed:
                grid[ky][kx] = pushed[(kx - dx, ky - dy)]
            else:
                grid[ky][kx] = '.'

        cx, cy = current_pos
        current_pos = (cx + dx, cy + dy)

score = 0
for y in range(N_ROWS):
    for x in range(N_COLS):
        if grid[y][x] == 'O':
            score += 100 * y + x

print(score)
print(time.time() - start_time)
