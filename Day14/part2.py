import time
from tqdm import tqdm
from collections import defaultdict
import re

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

N_ROWS = 103
N_COLS = 101
N_SECONDS = 1

positions = []
speeds = []

for line in lines:
    p, v = line.split(' ')
    px, py = [int(i) for i in p.split('=')[1].split(',')]
    vx, vy = [int(i) for i in v.split('=')[1].split(',')]

    positions.append((px, py))
    speeds.append((vx, vy))

new_positions = []


def get_repeats(line):
    if '#' not in line:
        return 0

    else:
        l = 1
        while re.search('#' * l, line):
            l += 1

        return l - 1


def display(index, poss, d=False):
    poset = set(poss)
    max_length = 0

    for y in range(N_ROWS):
        line = ''
        for x in range(N_COLS):
            if (x, y) in poset:
                line += '#'
            else:
                line += '.'
        if d:
            print(line.replace('#','■').replace('.','□'))

        max_length = max(max_length, get_repeats(line))

    return max_length


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

max_length = 0
index_s = None
for s in tqdm(range(101 * 103)):
    new_positions = []
    for pos, vel in zip(positions, speeds):
        px, py = pos
        vx, vy = vel

        nx, ny = ((px + s * vx) % N_COLS, (py + s * vy) % N_ROWS)
        new_positions.append((nx, ny))

    l = display(s, new_positions)
    if l > max_length:
        max_length = l
        s_index = s
        best_pos = new_positions.copy()

display(s_index, best_pos, True)
print(s_index)

print(time.time() - start_time)
