import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

n_rows = len(lines)
n_cols = len(lines[0])

words = ('MAS','SAM')

count = 0
for y in range(n_rows-2):
    for x in range(n_cols-2):
        word1 = ''.join(lines[j][i] for j,i in zip(range(y,y+3),range(x,x+3)))
        word2 = ''.join(lines[j][i] for j, i in zip(range(y, y + 3), range(x+2, x-1,-1)))

        if word1 in words and word2 in words:
            count+=1




print(count)
print(time.time() - start_time)
