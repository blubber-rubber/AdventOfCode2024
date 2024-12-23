import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

line = lines[0]

numbers = [int(x) for x in line]

result = []
for i, x in enumerate(numbers):
    if i % 2 == 0:
        result += [i // 2 for _ in range(x)]
    else:
        result += [None for _ in range(x)]

left_index = 0
right_index = len(result) - 1

while left_index < right_index:
    while result[left_index] is not None:
        left_index += 1

    while result[right_index] is None:
        right_index -= 1

    if left_index < right_index:
        result[left_index], result[right_index] = result[right_index], result[left_index]


print(sum(i*x for i,x in enumerate(result) if x is not None))

print(time.time() - start_time)
