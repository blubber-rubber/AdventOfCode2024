import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


def mix(a, b):
    return a ^ b


def prune(a):
    return a % 16777216


def result_a(s):
    return prune(mix(s, 64 * s))


def result_b(s):
    return prune(mix(s, s // 32))


def result_c(s):
    return prune(mix(s, 2048 * s))


def proc(s):
    return result_c(result_b(result_a(s)))


secret_numbers = []

som = 0
for line in lines:
    s = int(line)

    for _ in range(2000):
        s = proc(s)

    som += s

print(som)
print(time.time() - start_time)
