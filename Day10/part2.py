import time
from heapq import heapify, heappop, heappush
from collections import defaultdict

start_time = time.time()

with open('input.txt') as f:
    grid = [[int(c) for c in line.rstrip('\n')] for line in f.readlines()]

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N_ROWS = len(grid)
N_COLS = len(grid[0])

total_score = 0
for cy in range(N_COLS):
    for cx in range(N_ROWS):

        trail_score = 0

        if grid[cy][cx] == 0:
            start_pos = (cx,cy)
            act_visited = set()
            visited = defaultdict(int)
            visited[(cx, cy)] += 1
            heap = []
            heappush(heap, (grid[cy][cx], (cx, cy)))

            while heap:
                height, current_pos = heappop(heap)
                x, y = current_pos
                if current_pos not in act_visited:
                    act_visited.add(current_pos)
                    pos_score = 0
                    for dx, dy in DIRS:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < N_COLS and 0 <= ny < N_ROWS:
                            if grid[ny][nx] - height == 1 and (nx, ny) not in visited:
                                heappush(heap, (grid[ny][nx], (nx, ny)))
                            if grid[ny][nx] - height == -1 and (nx, ny) in visited:
                                pos_score += visited[(nx, ny)]
                    visited[(x, y)] += pos_score

                    if height == 9:
                        trail_score += visited[(x, y)]
            total_score += trail_score


print(total_score)

print(time.time() - start_time)
