import time
from collections import defaultdict
from heapq import heappush, heappop

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

DIRS = lines[0].split(', ')
longest_part = max(len(p) for p in DIRS)
longest_towel = max(len(t) for t in lines[2:])
sets = {x: set() for x in range(longest_towel+longest_part+1)}

for towel in lines[2:]:
    for x in range(len(towel)+1):
        sets[x].add(towel[:x])

scores = defaultdict(int)
scores[''] = 1

towels_of_length = defaultdict(set)
towels_of_length[0].add('')

length = 0

while length < longest_towel:
    for towel in towels_of_length[length]:
        for towel_part in DIRS:
            new_towel = towel + towel_part
            new_size = length + len(towel_part)
            if new_towel in sets[new_size]:
                scores[new_towel] += scores[towel]
                towels_of_length[new_size].add(new_towel)
    length += 1

possible = 0
for towel in lines[2:]:
    possible += scores[towel]

print(possible)
print(time.time() - start_time)
