import sys

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
    count = password.count(letter)
    if count <= interval[1] and count >= interval[0]:
        valid_passwords_count += 1

print(valid_passwords_count)