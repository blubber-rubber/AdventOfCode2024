import time
from collections import Counter
start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

print(len(lines))

list1 = []
list2 = []

for i, line in enumerate(lines):
    x,a,b,y = line.split(' ')

    list1.append(int(x))
    list2.append(int(y))

list1.sort(
)
list2.sort()

c = Counter(list2)


som = 0
for x in list1:
    som+= c[x]*x


print(som)



print(time.time() - start_time)
