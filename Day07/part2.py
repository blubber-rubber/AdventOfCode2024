import time
from itertools import product

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


def plus(a, b):
    return a + b


def mul(a, b):
    return a * b


def concat(a, b):
    return int(f'{a}{b}')


def dfs_operation(index, numbers, result, des_result):
    if index == len(numbers) - 1:
        return result == des_result

    for o in [plus, mul, concat]:
        new_result = o(result, numbers[index + 1])

        if new_result <= des_result:
            possible = dfs_operation(index + 1, numbers, new_result, des_result)
            if possible:
                return possible

    return False


som = 0

for line in lines:
    des_result, ns = line.split(': ')
    des_result = int(des_result)
    numbers = [int(x) for x in ns.split(' ')]

    possible = dfs_operation(0, numbers, numbers[0], des_result)

    if possible:
        som += des_result
print(som)
print(time.time() - start_time)
