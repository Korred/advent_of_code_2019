inp = '183564-657474'
start_range, end_range = map(int, inp.split('-'))


def check_conditions(pwd):
    # order should remain the same if going from left to right, the digits never decrease;
    cond1 = list(pwd) == sorted(pwd)

    # by using set() we can find it there are repetitions
    # condition 1 ensures ascending order, so pwds like '410524' -> {0, 1, 2, 4, 5} will not be accepted
    cond2 = len(set(pwd)) < len(pwd)

    return all([cond1, cond2])


possible_passwords = [pwd for pwd in range(start_range, end_range + 1) if check_conditions(str(pwd))]

print(len(possible_passwords))
