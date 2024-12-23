import time
from collections import defaultdict

start_time = time.time()

with open('input.txt') as f:
    grid = [[x for x in line.rstrip('\n')] for line in f.readlines()]

areas = defaultdict(int)

perimeters = defaultdict(int)

N_ROWS = len(grid)
N_COLS = len(grid[0])

visited = set()

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
price = 0
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if (x, y) not in visited:
            area = 0
            perimeter = 0
            stack = [(x, y)]

            while stack:
                cx, cy = stack.pop(0)
                if (cx,cy) not in visited:

                    visited.add((cx, cy))
                    area += 1
                    for dx, dy in dirs:
                        nx = cx + dx
                        ny = cy + dy

                        if 0 <= nx < N_COLS and 0 <= ny < N_ROWS:
                            if grid[ny][nx] == char:
                                if (nx, ny) not in visited:
                                    stack.append((nx, ny))
                            else:
                                perimeter += 1
                        else:
                            perimeter += 1

            print(char,area,perimeter)
            price += area * perimeter



print(price)
