memory = []

# read input data
with open('task_2_input.txt', 'r') as data:
    for line in data:
        memory.extend(map(int,line.split(',')))


def run_code(memory, noun=None, verb=None):
    # work on a copy of memory
    # do not modify original memory
    mem = memory[:]

    # modify memory using noun and verb values
    if noun:
        mem[1] = noun
    if verb:
        mem[2] = verb

    # ip = Instruction Pointer
    ip = 0

    while True:
        op_code = mem[ip]

        if op_code == 99:
            break
        else:
            param_1 = mem[mem[ip+1]]
            param_2 = mem[mem[ip+2]]

            if op_code == 1:
                res = param_1 + param_2
            elif op_code == 2:
                res = param_1 * param_2

            mem[mem[ip+3]] = res

            ip += 4

    return mem

values_found = False
for v in range(0,99):
    if values_found:
        break
    else:
        for n in range(0,99):
            executed_memory = run_code(memory, n, v)

            if executed_memory[0] == 19690720:
                print("Noun: ", n)
                print("Verb: ", v)
                print("Result: ", (100*n)+v)
                values_found = True
                break
