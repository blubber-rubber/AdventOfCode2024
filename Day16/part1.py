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

heappush(states, (0, start_pos, (1, 0)))

visited = set()

while states[0][1] != end_pos:
    d, cpos, cdir = heappop(states)
    if (cpos, cdir) not in visited:
        visited.add((cpos, cdir))

        cx, cy = cpos
        dx, dy = cdir
        nx, ny = cx + dx, cy + dy

        if 0 <= nx < N_COLS and 0 <= ny < N_ROWS and grid[ny][nx] != '#':
            heappush(states, (d + 1, (nx, ny), cdir))

        dir_index = dirs.index(cdir)

        for di in [-1, 1]:
            heappush(states, (d + 1000, (cx, cy), dirs[(dir_index + di) % 4]))


print(states[0])
print(time.time() - start_time)
