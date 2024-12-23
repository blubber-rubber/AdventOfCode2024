import math
import time
from collections import defaultdict
from heapq import heappush, heappop
from itertools import combinations

start_time = time.time()

with open('input.txt') as f:
    grid = [line.rstrip('\n') for line in f.readlines()]

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
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        for d1, d2 in combinations(dirs, 2):
            coming_from = (x + d1[0], y + d1[1])
            going_to = (x + d2[0], y + d2[1])

            if coming_from in distance_to_end and going_to in distance_to_end:
                saved = abs(distance_to_end[coming_from] - distance_to_end[going_to]) - 2
                if saved >= 100:
                    counter += 1

print(counter)
print(time.time() - start_time)
