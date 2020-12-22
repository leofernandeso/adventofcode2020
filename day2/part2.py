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
pos_count = 0
valid_passwords_count = 0
for (pos1, pos2), letter, password in cases:

    if password[pos1-1] == letter:
        pos_count += 1
    if password[pos2-1] == letter:
        pos_count += 1
    if pos_count == 1:
        valid_passwords_count += 1

    pos_count = 0

print(valid_passwords_count)
    