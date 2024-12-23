import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

line = lines[0]

numbers = [int(x) for x in line]

result = []
for i, x in enumerate(numbers):
    if x != 0:
        if i % 2 == 0:
            result.append((x, i // 2))
        else:
            result.append((x, None))

right_index = len(result) - 1
while right_index >= 0:
    if result[right_index][1] is not None:
        left_index = 0
        while right_index > left_index:
            if result[left_index][1] is None and result[left_index][0] >= result[right_index][0]:
                empty_space = result[left_index][0]
                file_size = result[right_index][0]
                result_size = empty_space - file_size

                result[left_index] = (result[right_index])
                result[right_index] = (file_size, None)

                if result_size > 0:
                    if result[left_index + 1][1] is None:
                        result[left_index + 1] = (result[left_index + 1][0] + result_size, None)
                    else:
                        result.insert(left_index + 1, (result_size, None))
                        right_index += 1

                if right_index + 1 < len(result) and result[right_index + 1][1] is None:
                    new_size = result[right_index + 1][0] + result[right_index][0]
                    result[right_index] = (new_size, None)
                    del result[right_index + 1]

                if right_index - 1 >= 0 and result[right_index - 1][1] is None:
                    new_size = result[right_index - 1][0] + result[right_index][0]
                    result[right_index - 1] = (new_size, None)
                    del result[right_index]

                left_index = right_index

            left_index += 1
    right_index -= 1

total_result = []

for aantal, value in result:
    total_result += [value for _ in range(aantal)]

print(sum(i*x for i,x in enumerate(total_result) if x is not None))
print(time.time() - start_time)
