import time
from collections import defaultdict
from shapely.geometry import Polygon
from shapely import union_all, normalize, simplify

start_time = time.time()

with open('input.txt') as f:
    grid = [[x for x in line.rstrip('\n')] for line in f.readlines()]

areas = defaultdict(int)

perimeters = defaultdict(int)

N_ROWS = len(grid)
N_COLS = len(grid[0])

visited = set()

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
price = 0
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if (x, y) not in visited:
            visited2 = set()
            area = 0
            stack = [(x, y)]

            while stack:
                cx, cy = stack.pop(0)
                if (cx, cy) not in visited:

                    visited.add((cx, cy))
                    visited2.add((cx,cy))
                    area += 1
                    for dx, dy in dirs:
                        nx = cx + dx
                        ny = cy + dy

                        if 0 <= nx < N_COLS and 0 <= ny < N_ROWS:
                            if grid[ny][nx] == char:
                                if (nx, ny) not in visited:
                                    stack.append((nx, ny))



            boxes = [Polygon([(cx, cy), (cx + 1, cy), (cx + 1, cy + 1), (cx, cy + 1)]) for cx, cy in visited2]
            total_box = simplify(normalize(union_all(boxes)),0.1)

            edges = sum([len(total_box.exterior.coords)-1] + [len(hole.coords)-1 for hole in total_box.interiors])
            price+=edges * area


print(price)
