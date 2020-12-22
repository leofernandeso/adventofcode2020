import sys
import itertools

def parse_input():
    return [int(e) for e in sys.stdin]

expenses = parse_input()

result = None
for n1, n2 in itertools.combinations(expenses, r=2):
    if n1 + n2 == 2020:
        result = n1 * n2

print(result)
