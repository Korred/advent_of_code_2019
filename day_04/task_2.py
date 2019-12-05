import re

pattern_1 = re.compile(r'(.)\1{2,}')
pattern_2 = re.compile(r'(.)\1{1}')

inp = '183564-657474'
start_range, end_range = map(int, inp.split('-'))


def check_conditions(pwd):
    # order should remain the same if going from left to right, the digits never decrease;
    cond1 = list(pwd) == sorted(pwd)

    # remove larger groups first
    # check if two adjacent matcheing digits remain
    cond2 = pattern_2.search(pattern_1.sub('', pwd))

    return all([cond1, cond2])


possible_passwords = [pwd for pwd in range(start_range, end_range + 1) if check_conditions(str(pwd))]

print(len(possible_passwords))

