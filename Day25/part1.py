import time
from itertools import product

start_time = time.time()

with open('input.txt') as f:
    parts = [line.rstrip('\n') for line in ''.join(f.readlines()).split('\n\n')]

keys = []
locks = []

for part in parts:
    layers = part.split('\n')
    N_COLS = len(layers[0])
    N_ROWS = len(layers)

    if layers[0] == '#' * N_COLS:
        locks.append(
            tuple(len([layers[i][j] for i in range(len(layers)) if layers[i][j] == '#']) for j in range(N_COLS)))

    else:
        keys.append(
            tuple(len([layers[i][j] for i in range(len(layers)) if layers[i][j] == '#']) for j in range(N_COLS)))

count = 0
print(len(keys) * len(locks))
for key, lock in product(keys, locks):
    if all(x + y <= N_ROWS for x, y in zip(key, lock)):
        count += 1
        # print(lock, key)

print(count)

print(time.time() - start_time)
