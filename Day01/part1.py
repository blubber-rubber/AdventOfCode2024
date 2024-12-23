import time

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

som = 0
for x,y in zip(list1,list2):
    som += abs(x-y)


print(som)



print(time.time() - start_time)
