import re

inp = '183564-657474'
start_range, end_range = map(int, inp.split('-'))

possible_passwords = []

pattern_1 = re.compile(r'(.)\1{2,}')
pattern_2 = re.compile(r'(.)\1{1}')

for password in range(start_range, end_range + 1):
    str_pw = str(password)
    invalid_pw = False
    adjacent_found = False

    # Going from left to right, the digits never decrease;
    for a, b in zip(str_pw, str_pw[1:]):
        if int(a) > int(b):
            invalid_pw = True
            break

    # the two adjacent matching digits are not part of a larger group of matching digits
    if not invalid_pw:
        # remove larger groups first
        sub_pw = pattern_1.sub('', str_pw)

        # check if two adjacent matcheing digits remain
        if pattern_2.search(sub_pw):
            adjacent_found = True

    if not invalid_pw and adjacent_found:
        possible_passwords.append(str_pw)


print(len(possible_passwords))
