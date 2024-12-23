import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

N_ROWS = 103
N_COLS = 101
N_SECONDS = 100

positions = []
speeds = []

for line in lines:
    p, v = line.split(' ')
    px, py = [int(i) for i in p.split('=')[1].split(',')]
    vx, vy = [int(i) for i in v.split('=')[1].split(',')]

    positions.append((px, py))
    speeds.append((vx, vy))

new_positions = []

qs = [0, 0, 0, 0]

for pos, vel in zip(positions, speeds):
    px, py = pos
    vx, vy = vel

    nx, ny = ((px + N_SECONDS * vx) % N_COLS, (py + N_SECONDS * vy) % N_ROWS)
    new_positions.append((nx, ny))

    if nx < N_COLS // 2 and ny < N_ROWS // 2:
        qs[0] += 1
        print(0, (nx, ny))
    elif nx > (N_COLS // 2) and ny < N_ROWS // 2:
        qs[1] += 1
        print(1, (nx, ny))
    elif nx < N_COLS // 2 and ny > N_ROWS // 2:
        qs[2] += 1
        print(2, (nx, ny))
    elif nx > N_COLS // 2 and ny > N_ROWS // 2:
        qs[3] += 1
        print(3, (nx, ny))
    else:
        print(-1, (nx, ny))

print(qs[0] * qs[1] * qs[2] * qs[3])
print(time.time() - start_time)
