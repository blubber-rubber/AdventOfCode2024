import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

n_rows = len(lines)
n_cols = len(lines[0])

count = 0
for j in range(n_rows):
    for i in range(n_cols - 3):
        print(lines[j][i:i + 4])
        if lines[j][i:i + 4] in ('XMAS', 'SAMX'):
            count += 1
    print('-----')

for i in range(n_cols):
    for j in range(n_rows - 3):
        if ''.join(line[i] for line in lines[j:j + 4]) in ('XMAS', 'SAMX'):
            count += 1

for j in range(n_rows - 3):
    for i in range(n_rows - 3):
        if ''.join(lines[y][x] for y, x in zip(range(j, j + 4), range(i, i + 4))) in ('XMAS', 'SAMX'):
            count += 1

for j in range(n_rows - 3):
    for i in range(3, n_rows):
        if ''.join(lines[y][x] for y, x in zip(range(j, j + 4), range(i , i-4,-1))) in ('XMAS', 'SAMX'):
            count += 1

print(count)
print(time.time() - start_time)
