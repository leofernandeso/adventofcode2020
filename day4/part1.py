import sys

def parse_input():

    def parse_passport(content):
        passport = {}
        for pair in content.strip().replace('\n', ' ').split(' '):
            k, v = pair.split(':')
            passport[k] = v
        return passport

    passports = []
    content = ''
    for line in sys.stdin:
        if line != '\n':
            content += line
        else:
            passports.append(parse_passport(content))
            content = ''
    passports.append(parse_passport(content))
    return passports

required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
optional = 'cid'

passports = parse_input()
valid_count = 0
for passport in passports:
    fields = passport.keys()
    missing_count = len(required_fields.difference(set(fields)))
    if missing_count == 0 or (missing_count == 1 and optional not in fields):
        valid_count += 1

print(valid_count)
    


        

