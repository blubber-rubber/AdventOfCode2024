import math
import time
from heapq import heappop, heappush

start_time = time.time()

with open('input.txt') as f:
    grid = [[x for x in line.rstrip('\n')] for line in f.readlines()]

N_ROWS = len(grid)
N_COLS = len(grid[0])

start_pos = [(x, y) for x in range(N_COLS) for y in range(N_ROWS) if grid[y][x] == 'S'][0]
end_pos = [(x, y) for x in range(N_COLS) for y in range(N_ROWS) if grid[y][x] == 'E'][0]

states = []

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

heappush(states, (0, start_pos, (1, 0), [start_pos]))

from collections import defaultdict

visited = defaultdict(lambda: math.inf)

good_ones = []
best_path = math.inf

while states[0][0] <= best_path:
    d, cpos, cdir, prevs = heappop(states)

    if cpos == end_pos:
        if d <= best_path:
            best_path = d
            good_ones.append(prevs)

    if d <= visited[(cpos, cdir)] and d <= best_path:
        visited[(cpos, cdir)] = d

        cx, cy = cpos
        dx, dy = cdir
        nx, ny = cx + dx, cy + dy

        if 0 <= nx < N_COLS and 0 <= ny < N_ROWS and grid[ny][nx] != '#':
            new_prevs = prevs.copy()
            new_prevs.append((nx, ny))
            heappush(states, (d + 1, (nx, ny), cdir, new_prevs))

        dir_index = dirs.index(cdir)

        for di in [-1, 1]:
            heappush(states, (d + 1000, (cx, cy), dirs[(dir_index + di) % 4], prevs))

total = set()
for path in good_ones:
    total = total.union(path)
print(len(total))

print(time.time() - start_time)
