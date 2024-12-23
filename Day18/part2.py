import math
import time
from collections import defaultdict
from heapq import heappush, heappop

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

size = 70

walls = set()

fallen_bytes = 1024

for line in lines[:fallen_bytes]:
    x, y = (int(i) for i in line.split(','))
    walls.add((x, y))


def heuristic(p):
    return size - p[0] + size - p[1]


def try_maze():
    states = []
    start_pos = (0, 0)
    heappush(states, (heuristic(start_pos), 0, start_pos, [start_pos]))
    visited = defaultdict(lambda: math.inf)
    visited[start_pos] = 0

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while states and states[0][2] != (size, size):
        h, d, p, path = heappop(states)
        cx, cy = p
        if d <= visited[p]:
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                new_pos = (nx, ny)
                if 0 <= nx <= size and 0 <= ny <= size and d + 1 < visited[new_pos] and new_pos not in walls:
                    new_path = path.copy()
                    new_path.append(new_pos)
                    visited[(nx, ny)] = d + 1
                    heappush(states, (d + 1 + heuristic(new_pos), d + 1, new_pos, new_path))

    if not states:
        return False, None
    return True, states[0][3]


possible, lijst = try_maze()

while possible:
    wx, wy = (int(i) for i in lines[fallen_bytes].split(','))
    walls.add((wx, wy))

    while (wx, wy) not in lijst:
        fallen_bytes += 1
        wx, wy = (int(i) for i in lines[fallen_bytes].split(','))
        walls.add((wx, wy))

    possible, lijst = try_maze()

print(f'{wx},{wy}', fallen_bytes)


print(time.time() - start_time)
