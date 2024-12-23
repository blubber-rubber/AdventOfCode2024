import time

start_time = time.time()

with open('input.txt') as f:
    grid = [[int(c) for c in line.rstrip('\n')] for line in f.readlines()]

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N_ROWS = len(grid)
N_COLS = len(grid[0])


def dfs(current_pos, grid, visited):
    if current_pos in visited:
        return 0

    visited.add(current_pos)
    x, y = current_pos

    height = grid[y][x]

    if height == 9:
        return 1

    score = 0
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N_COLS and 0 <= ny < N_ROWS and grid[ny][nx] - height == 1:
            score += dfs((nx, ny), grid, visited)

    return score


total_score = 0
for y in range(N_COLS):
    for x in range(N_ROWS):
        if grid[y][x] == 0:
            visited = set()
            total_score += dfs((x, y), grid, visited)

print(total_score)

print(time.time() - start_time)
