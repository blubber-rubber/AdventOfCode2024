import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


class Node:

    def __init__(self):
        self.next = None
        self.value = None
        self.previous = None

    def __repr__(self):
        return f'Node({self.value})'

    def change_node(self):
        result = []
        val = str(self.value)
        if self.value == 0:
            self.value = 1
            result = [self]

        elif len(val) % 2 == 0:
            nn1 = Node()
            nn2 = Node()

            nn1.next = nn2
            nn2.previous = nn1

            nn1.value = int(val[:len(val) // 2])
            nn2.value = int(val[len(val) // 2:])

            result = [nn1, nn2]

        else:
            self.value = 2024 * self.value
            result = [self]

        return result


numbers = [int(x) for x in lines[0].split(' ')]

start_node = Node()
start_node.value = numbers[0]

current_node = start_node

for x in numbers[1:]:
    new_node = Node()
    current_node.next = new_node
    new_node.value = x
    new_node.previous = current_node
    current_node = new_node


for _ in range(25):
    next_node = start_node.next
    first_change = start_node.change_node()

    start_node = first_change[0]
    first_change[-1].next = next_node
    next_node.previous = first_change[-1]
    current_node = next_node

    while current_node is not None:
        prev_node = current_node.previous
        next_node = current_node.next

        changes = current_node.change_node()

        changes[0].previous = prev_node
        if prev_node:
            prev_node.next = changes[0]

        changes[-1].next = next_node
        if next_node:
            next_node.previous = changes[-1]

        current_node = next_node



cn = start_node
counter = 0
while cn is not None:
    counter += 1
    cn = cn.next

print(time.time()-start_time)
print(counter)
