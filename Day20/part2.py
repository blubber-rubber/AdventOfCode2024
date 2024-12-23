import math
import time
from collections import defaultdict
from heapq import heappush, heappop
from itertools import combinations

start_time = time.time()

with open('input.txt') as f:
    grid = [line.rstrip('\n') for line in f.readlines()]


CHEAT_SECONDS = 100
N_ROWS = len(grid)
N_COLS = len(grid[0])

for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == 'S':
            start_pos = (x, y)
        if c == 'E':
            end_pos = (x, y)

states = []
heappush(states, (0, end_pos))

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

distance_to_end = defaultdict(lambda: math.inf)
distance_to_end[end_pos] = 0

while states and states[0][1] != start_pos:
    d, p = heappop(states)
    cx, cy = p
    for dx, dy in dirs:
        nx, ny = cx + dx, cy + dy
        new_pos = (nx, ny)
        if 0 <= nx < N_COLS and 0 <= ny < N_ROWS and grid[ny][nx] != '#' and d + 1 < distance_to_end[new_pos]:
            distance_to_end[new_pos] = d + 1
            heappush(states, (d + 1, new_pos))

counter = 0
for start_pos in distance_to_end:
    cx, cy = start_pos
    for dx in range(-CHEAT_SECONDS, CHEAT_SECONDS+1):
        rest_seconds = CHEAT_SECONDS - abs(dx)
        for dy in range(-rest_seconds, rest_seconds + 1):
            nx, ny = cx + dx, cy + dy
            if (nx, ny) in distance_to_end:
                time_saved = distance_to_end[(cx, cy)] - distance_to_end[(nx, ny)] - (abs(dx) + abs(dy))

                if time_saved >= 100:
                    counter += 1
print(counter)
print(time.time() - start_time)
