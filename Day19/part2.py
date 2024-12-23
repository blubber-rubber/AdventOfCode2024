import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

DIRS = lines[0].split(', ')

WAYS = {'': 1}


def construct_towel(desired_towel):
    if desired_towel not in WAYS:
        ways = 0
        for d in DIRS:
            if desired_towel.startswith(d):
                ways += construct_towel(desired_towel[len(d):])

        WAYS[desired_towel] = ways

    return WAYS[desired_towel]


possible = 0
for towel in lines[2:]:
    possible += construct_towel(towel)

print(possible)
print(time.time() - start_time)
