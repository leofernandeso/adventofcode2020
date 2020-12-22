import sys
import itertools
from functools import reduce

def parse_input():
    return [int(e) for e in sys.stdin]

# Reading input
expenses = parse_input()

# Getting params from cmd line
n = int(sys.argv[1])             # nr of entries that sum up to 'criteria' (for part1 = 2 and for part2 = 3)
criteria = int(sys.argv[2])      # 2020 in parts 1 and 2

result = None
for numbers in itertools.combinations(expenses, r=n):
    if sum(numbers) == criteria:
        result = reduce(lambda x, y: x * y, numbers)

print(result)
