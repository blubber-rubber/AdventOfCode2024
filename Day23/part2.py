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


def build_subgraph(subgraph, neighbours: set, visited):
    if not neighbours:
        return tuple(sorted(subgraph))

    best_sub = None
    best_l = 0
    for n in neighbours:
        subgraph.append(n)

        if tuple(sorted(subgraph)) not in visited:

            neighbours.remove(n)
            new_neighbours = neighbours.intersection(graph[n])
            sub = build_subgraph(subgraph, new_neighbours, visited)
            visited[tuple(sorted(subgraph))] = sub
            if len(sub) > best_l:
                best_sub = sub
            neighbours.add(n)

        else:
            sub = visited[tuple(sorted(subgraph))]
            if len(sub) > best_l:
                best_sub = sub

        del subgraph[-1]

    # visited[tuple(sorted(subgraph))] = best_sub
    return best_sub


visited = {}
best_sub = None
best_l = 0
for a, ns in graph.items():
    subgraph = [a]
    large_subgraph = build_subgraph(subgraph, ns, visited)
    if len(large_subgraph)>best_l:
        best_sub = large_subgraph
        best_l = len(large_subgraph)

print(','.join(best_sub))
print(time.time() - start_time)
