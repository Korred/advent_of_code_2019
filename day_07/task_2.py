from itertools import permutations
from collections import deque

memory = []

# read input data
with open('task_1_input.txt', 'r') as data:
    for line in data:
        memory.extend(map(int, line.split(',')))


def run_code(program, inp, pointer=0):
    mem = program[:]

    # ip = Instruction Pointer
    ip = pointer

    output = None

    while True:
        # pad istruction_code with zeros
        ic = '0' * (5 - len(str(mem[ip]))) + str(mem[ip])
        op_code = int(ic[-2:])
        param_modes = [int(mode) for mode in ic[:-2][::-1]]

        if op_code == 99:
            # exit code 0 = success/completed
            return (0, mem, output, ip)

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

            if len(inp) == 0:
                # exit code 1 = running/waiting for input
                return (1, mem, output, ip)

            # read from input and save
            mem[mem[ip + 1]] = inp.pop(0)

            # increase instruction pointer by 2
            ip += 2

        # read data and output
        if op_code == 4:
            output = mem[mem[ip + 1]] if param_modes[0] == 0 else mem[ip + 1]

            # increase instruction pointer by 2
            ip += 2

            # exit code 2 = running/providing output
            return (2, mem, output, ip)

        # jump-if-true
        if op_code == 5:
            # read param values according to param_mode
            p1 = mem[mem[ip + 1]] if param_modes[0] == 0 else mem[ip + 1]
            p2 = mem[mem[ip + 2]] if param_modes[1] == 0 else mem[ip + 2]

            if p1 != 0:
                ip = p2
            else:
                ip += 3

        # jump-if-false
        if op_code == 6:
            # read param values according to param_mode
            p1 = mem[mem[ip + 1]] if param_modes[0] == 0 else mem[ip + 1]
            p2 = mem[mem[ip + 2]] if param_modes[1] == 0 else mem[ip + 2]

            if p1 == 0:
                ip = p2
            else:
                ip += 3

        # less than
        if op_code == 7:
            p1 = mem[mem[ip + 1]] if param_modes[0] == 0 else mem[ip + 1]
            p2 = mem[mem[ip + 2]] if param_modes[1] == 0 else mem[ip + 2]
            p3 = mem[ip + 3]

            if p1 < p2:
                mem[p3] = 1
            else:
                mem[p3] = 0

            ip += 4

        # equals
        if op_code == 8:
            p1 = mem[mem[ip + 1]] if param_modes[0] == 0 else mem[ip + 1]
            p2 = mem[mem[ip + 2]] if param_modes[1] == 0 else mem[ip + 2]
            p3 = mem[ip + 3]

            if p1 == p2:
                mem[p3] = 1
            else:
                mem[p3] = 0

            ip += 4


# feedback mode
max_signal = 0
for perm in permutations(range(5, 10), 5):
    input_signal = 0
    waiting = deque()

    # init aplifieres
    for amp in range(5):
        response = run_code(memory, [perm[amp]])
        # print(f"AMP {amp}: exit code {response[0]}")
        waiting.append(response)

    while waiting:
        amp = waiting.popleft()
        response = run_code(amp[1], [input_signal], amp[3])

        # waiting for input
        if response[0] == 1:
            waiting.append(response)

        # providing output
        if response[0] == 2:
            input_signal = response[2]
            waiting.append(response)

        # for w in waiting:
        #    print(w)
        # input()

    # feedback runs

    if input_signal > max_signal:
        max_signal = input_signal


print(max_signal)
