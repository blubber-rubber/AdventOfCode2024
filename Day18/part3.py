import math
import time
from collections import defaultdict
from heapq import heappush, heappop

start_time = time.time()
grid_scores = defaultdict(lambda: math.inf)

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

size =70

for index, line in enumerate(lines):
    x, y = (int(i) for i in line.split(','))
    grid_scores[(x, y)] = index

states = []
start_pos = (0, 0)
heappush(states, (-grid_scores[start_pos], start_pos))
visited = defaultdict(lambda: math.inf)
visited[start_pos] = 0

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while states and states[0][1] != (size, size):
    s, p, = heappop(states)
    cx, cy = p
    if s <= visited[p]:
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            new_pos = (nx, ny)
            new_score = max(-grid_scores[new_pos], s)
            if 0 <= nx <= size and 0 <= ny <= size and new_score < visited[new_pos]:
                visited[new_pos] = new_score
                heappush(states, (new_score, new_pos))

print(lines[-states[0][0]])

print(time.time() - start_time)
