import sys
from collections import Counter

def parse_input():

    # Function for parsing each line of the input
    def parse_line(line):
        interval, letter, password = line.split(' ')
        interval = tuple(map(int, interval.split('-')))
        letter = letter[0]
        password = password.strip()
        return interval, letter, password

    cases = []
    for line in sys.stdin:
        cases.append(parse_line(line))
    return cases

cases = parse_input()
valid_passwords_count = 0
for interval, letter, password in cases:
    counts = Counter(password)
    if counts[letter] <= interval[1] and counts[letter] >= interval[0]:
        valid_passwords_count += 1

print(valid_passwords_count)
    