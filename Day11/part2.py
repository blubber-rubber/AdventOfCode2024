import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

numbers = [int(x) for x in lines[0].split(' ')]

CACHE = {}


def dfs(depth, value):
    if depth == 75:
        CACHE[(depth, value)] = 1

    if (depth, value) not in CACHE:
        n_stones = 0
        val = str(value)
        if value == 0:
            n_stones = dfs(depth + 1, 1)
        elif len(val) % 2 == 0:
            n_stones += dfs(depth + 1, int(val[:len(val) // 2]))
            n_stones += dfs(depth + 1, int(val[len(val) // 2:]))
        else:
            n_stones += dfs(depth + 1, 2024 * value)
        CACHE[(depth,value)] = n_stones
    return CACHE[(depth, value)]


total = 0
for n in numbers:
    total += dfs(0, n)


print(time.time()-start_time)
print(len(CACHE.items()))
print(total)
