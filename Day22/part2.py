import time
from collections import defaultdict
from itertools import product

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


def mix(a, b):
    return a ^ b


def prune(a):
    return a % 16777216


def result_a(s):
    return prune(mix(s, 64 * s))


def result_b(s):
    return prune(mix(s, s // 32))


def result_c(s):
    return prune(mix(s, 2048 * s))


def proc(s):
    return result_c(result_b(result_a(s)))


best_deals = defaultdict(list)

buyers = []
for buyer_index, line in enumerate(lines):
    s = int(line)
    prices = [s % 10]

    for c in product(range(-9, 10), repeat=4):
        best_deals[c].append(None)

    s = int(line)
    for _ in range(2000):
        s = proc(s)
        prices.append(s % 10)

    price_changes = [b - a for a, b in zip(prices, prices[1:])]
    for price_change_index in range(len(price_changes) - 3):
        relevant_changes = price_changes[price_change_index:price_change_index + 4]
        relevant_price = prices[4 + price_change_index]

        c = tuple(relevant_changes)
        if best_deals[c][buyer_index] is None:
            best_deals[c][buyer_index] = relevant_price

best_sequence = max(best_deals.items(), key=lambda x: sum(p for p in x[1] if p is not None))

print(sum(p for p in best_sequence[1] if p is not None))
print(best_sequence)
print(time.time() - start_time)
