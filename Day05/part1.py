import time
from itertools import combinations

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


split_index = [i for i in range(len(lines)) if lines[i]==''][0]

instr = lines[:split_index]

updates = lines[split_index+1:]

instructions = {(int(i.split('|')[0]),int(i.split('|')[1]))  for i in instr}


som = 0
for line in updates:
    numbers = [int(i) for i in  line.split(',')]
    forbidden = {(int(y),int(x)) for x,y in combinations(numbers,2)}

    if not forbidden.intersection(instructions):
       som+= numbers[len(numbers)//2]

print(som)
print(time.time() - start_time)
