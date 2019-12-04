inp = '183564-657474'
start_range, end_range = map(int, inp.split('-'))

possible_passwords = []

for password in range(start_range, end_range + 1):
    str_pw = str(password)
    invalid_pw = False
    adjacent_found = False

    # Going from left to right, the digits never decrease;
    for a, b in zip(str_pw, str_pw[1:]):
        if int(a) > int(b):
            invalid_pw = True
            break

        if a == b:
            adjacent_found = True

    if not invalid_pw and adjacent_found:
        possible_passwords.append(str_pw)


print(len(possible_passwords))
