import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

n_safe = 0
for line in lines:
    safe = True

    numbers = [int(x) for x in line.split(' ')]

    i = 1

    increasing = numbers[0] < numbers[1]


    while i < len(numbers) and safe:
        safe = safe and 1 <= abs(numbers[i - 1] - numbers[i]) <= 3

        if increasing:
            safe = safe and numbers[i - 1] < numbers[i]
        else:
            safe = safe and numbers[i - 1] > numbers[i]
        i += 1

    if safe:
        n_safe += 1

print(n_safe)
print(time.time() - start_time)
