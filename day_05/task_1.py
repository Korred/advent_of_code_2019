memory = []

# read input data
with open('task_1_input.txt', 'r') as data:
    for line in data:
        memory.extend(map(int, line.split(',')))


def run_code(program, inp):
    mem = program[:]

    # ip = Instruction Pointer
    ip = 0

    while True:
        # pad istruction_code with zeros
        ic = '0' * (5 - len(str(mem[ip]))) + str(mem[ip])
        op_code = int(ic[-2:])
        param_modes = [int(mode) for mode in ic[:-2][::-1]]

        if op_code == 99:
            break

        # addition
        if op_code == 1:

            # read param values according to param_mode
            p1 = mem[mem[ip + 1]] if param_modes[0] == 0 else mem[ip + 1]
            p2 = mem[mem[ip + 2]] if param_modes[1] == 0 else mem[ip + 2]
            p3 = mem[ip + 3]

            # add values
            res = p1 + p2

            # save value at provided memory position
            mem[p3] = res

            # increase instruction pointer by 4
            ip += 4

        # multiplication
        if op_code == 2:
            # read param values according to param_mode
            p1 = mem[mem[ip + 1]] if param_modes[0] == 0 else mem[ip + 1]
            p2 = mem[mem[ip + 2]] if param_modes[1] == 0 else mem[ip + 2]
            p3 = mem[ip + 3]

            # multiply values
            res = p1 * p2

            # save value at provided memory position
            mem[p3] = res

            # increase instruction pointer by 4
            ip += 4

        # read input and save
        if op_code == 3:
            # read from input and save
            mem[mem[ip + 1]] = inp.pop(0)

            # increase instruction pointer by 2
            ip += 2

        # read data and output
        if op_code == 4:
            out = mem[mem[ip + 1]] if param_modes[0] == 0 else mem[ip + 1]

            # output data
            print(f"Output: {out}")

            # increase instruction pointer by 2
            ip += 2

    return mem


run_code(memory, [1])

