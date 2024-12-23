import time
from collections import defaultdict

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

graph = defaultdict(set)

for line in lines:
    a, b = line.split('-')
    graph[a].add(b)
    graph[b].add(a)

sols = set()

for a, ns in graph.items():
    for b in ns:
        for c in ns.intersection(graph[b]):
            triplet = tuple(sorted([a, b, c]))
            if any(x.startswith('t') for x in triplet):
                sols.add(triplet)

print(len(sols))
print(time.time() - start_time)
