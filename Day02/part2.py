import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

n_safe = 0
for line in lines:


    all_numbers = [int(x) for x in line.split(' ')]

    final_save = False

    for j in range(len(all_numbers)):

        numbers = all_numbers[:j] + all_numbers[j + 1:]

        i = 1

        increasing = numbers[0] < numbers[1]
        safe = True
        while i < len(numbers) and safe:
            safe = safe and 1 <= abs(numbers[i - 1] - numbers[i]) <= 3

            if increasing:
                safe = safe and numbers[i - 1] < numbers[i]
            else:
                safe = safe and numbers[i - 1] > numbers[i]
            i += 1

        if safe:
            final_save = True

    n_safe += final_save

print(n_safe)
print(time.time() - start_time)
