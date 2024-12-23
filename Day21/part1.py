import math
import time
from collections import defaultdict
from itertools import product
from functools import lru_cache

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+
"""

numeric_keypad = ['789', '456', '123', ' 0A']

"""
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""

direction_keypad = [' ^A', '<v>']


def get_paths(grid, DIRS):
    n_rows = len(grid)
    n_cols = len(grid[0])
    grid_paths = defaultdict(list)
    for y in range(n_rows):
        for x in range(n_cols):
            if grid[y][x] != ' ':
                grid_paths[(grid[y][x], grid[y][x])] = ['']
                start_pos = (x, y)
                states = [(start_pos, [])]
                visited = defaultdict(lambda: math.inf)
                visited[start_pos] = 0
                while states:
                    cp, path = states.pop(0)
                    cx, cy = cp
                    if len(path) <= visited[cp]:
                        for key, d in DIRS.items():
                            dx, dy = d
                            nx, ny = cx + dx, cy + dy
                            new_pos = (nx, ny)
                            if 0 <= nx < n_cols and 0 <= ny < n_rows and grid[ny][
                                nx] != ' ' and len(path) + 1 <= visited[new_pos]:
                                visited[new_pos] = len(path) + 1
                                new_path = path.copy()
                                new_path.append(key)
                                grid_paths[(grid[y][x], grid[ny][nx])].append(''.join(new_path))
                                states.append((new_pos, new_path))
    minimal_grid_paths = {x: y[0] for x, y in grid_paths.items()}
    return grid_paths


DIRS = {'>': (1, 0), '^': (0, -1), '<': (-1, 0), 'v': (0, 1)}
num_keypad_paths = get_paths(numeric_keypad, DIRS)
DIRS = {'>': (1, 0), 'v': (0, 1), '<': (-1, 0), '^': (0, -1)}
dir_keypad_paths = get_paths(direction_keypad, DIRS)




def expand_dir_seq(seq, paths):
    expanded_seq = []
    products = []
    for start_pos, end_pos in zip('A' + seq, seq):
        products.append(paths[(start_pos, end_pos)])

    for point in product(*products):
        expanded_seq.append('A'.join(point) + 'A')
    return expanded_seq


result = 0
for line in lines:
    seqs = []
    for seq1 in expand_dir_seq(line, num_keypad_paths):
        for seq2 in expand_dir_seq(seq1, dir_keypad_paths):
            for seq3 in expand_dir_seq(seq2, dir_keypad_paths):
                seqs.append(seq3)

    shortest = min(seqs, key=lambda l: len(l))
    value = int(line[:-1])
    result += len(shortest) * value

print(result)
#
#
# #v<<A >>^A vA ^A v<<A>>^AAv<A<A>>^AAvAA<^A>Av<A>^AA<A>Av<A<A>>^AAAvA<^A>A
# #<v<A >>^A vA ^A <vA <A A >>^A A vA <^A >A A vA ^A <vA >^A A <A >A <v<A >A >^A A A vA <^A >A
#
# #<A >A <A A v<A A >>^A vA A ^A v<A A A >^A
# #<A >A v<<A A >^A A >A vA A ^A <vA A A >^A
#
# #^A^^<<A>>AvvvA
# #^A<<^^A>>AvvvA
#
#
# #v<<A >>^A A v<A <A >>^A A vA A <^A >A
# #<vA <A A >>^A A vA <^A >A A vA ^A
#
# #33 0 213 0 1021
# #<A A v<A A >>^A
# #2103 0 121 0 11
# #v<<A A >^A A >A
#
# #^^<<A
# #<<^^A
#
#
# #v<<A >>^A v<A <A >>^A vA A <^A >A
# #<vA <A A >>^A vA <^A >A vA ^A
#
# #33 213 1021
# #<A v<A >>^A
# #2103 121 11
# #v<<A >^A >A
#
# #^<A
# #<^A
