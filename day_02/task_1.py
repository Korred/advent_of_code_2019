intcode = []

# read input data
with open('task_2_input.txt', 'r') as data:
    for line in data:
        intcode.extend(map(int,line.split(',')))

# replace position 1 with the value 12
intcode[1] = 12

# replace position 2 with the value 2
intcode[2] = 2

def run_intcode(intcode):
    pos = 0
    while True:
        op_code = intcode[pos]

        if op_code == 99:
            break
        else:
            inp_1 = intcode[intcode[pos+1]]
            inp_2 = intcode[intcode[pos+2]]

            if op_code == 1:
                res = inp_1 + inp_2
            elif op_code == 2:
                res = inp_1 * inp_2

            intcode[intcode[pos+3]] = res

            pos += 4

    return intcode


executed_intcode = run_intcode(intcode)
print(intcode[0])