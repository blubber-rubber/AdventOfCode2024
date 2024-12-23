import time
import math

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


# a * k1 + b * l1 = x
# a * k2 + b * l2= y

# a = (x-b*l1)/k1
#  k2*(x-b*l1)/k1 + b*l2 = y

# a = (x-b*l1)/k1
#  k2/k1*x-k2/k1*b*l1 + b*l2 = y

# a = (x-b*l1)/k1
#  b = (y - k2/k1*x)/(-k2/k1*l1 + l2)


# a * 94 + b*22 = 8400
# a*34 + b*67 = 5400

# a  =

lines.append('')
index = 0
tokens = 0

check = {}

for index in range(len(lines) // 4):
    b1, b2, p, _ = lines[4 * index:4 * index + 4]
    print(lines[4 * index:4 * index + 4])

    _, k1, k2 = b1.split('+')
    k1 = int(k1.split(',')[0])
    k2 = int(k2)

    _, l1, l2 = b2.split('+')
    l1 = int(l1.split(',')[0])
    l2 = int(l2)

    _, x, y = p.split('=')
    x = int(x.split(',')[0])
    y = int(y)

    #  b  = (5400 - 8400/94*34)/(- 22/94*34 + 67)
    b = (y*k1 - x * k2) / (-l1 * k2 + l2 * k1)
    a = (x - b * l1) / k1

    if 0 <= a <= 100 and 0 <= b <= 100:
        ar = round(a)
        br = round(b)
        tr = 3 * ar + br
        if ar * k1 + br * l1 == x and ar * k2 + br * l2 == y:
            tokens += tr
            check[index] = tr

print(tokens)
print(time.time() - start_time)
