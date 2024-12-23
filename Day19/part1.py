import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

DIRS = lines[0].split(', ')


def construct_towel(current_towel, desired_towel):
    if len(current_towel) == len(desired_towel):
        return True

    rest_towel = desired_towel[len(current_towel):]

    for d in DIRS:
        if len(d) <= len(rest_towel) and rest_towel[:len(d)] == d:
            result = construct_towel(current_towel + d, desired_towel)
            if result:
                return result

    return False


possible = 0
for towel in lines[2:]:
    if construct_towel('', towel):
        possible += 1

print(possible)
print(time.time() - start_time)
