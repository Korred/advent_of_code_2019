import sys

sys.path.append("..")
from utils.utils import IntComputer, Program

mem = list(map(int, open('task_1_input.txt', 'r').readline().split(',')))
# free game hack :D
mem[0] = 2

int_comp = IntComputer()
int_comp.add_program(Program(mem, []))

# ball pos
b_x, b_y = 0, 0

# paddle pos
p_x, p_y = 0, 0

while int_comp.programs[0].status != 0:
    int_comp.run_prog()
    status = int_comp.programs[0].status

    # run until status is not 2 (output)
    if status == 2:
        continue

    # parse output
    output = int_comp.programs[0].outputs
    instructions = [output[i : i + 3] for i in range(0, len(output), 3)]

    # execute instructions
    for i in instructions:
        x, y, tile = i

        # display score
        if x == -1 and y == 0:
            print(f'Score: {tile}')
            continue

        # only track ball and paddle
        # blocks are irrelevant

        # set paddle pos
        if tile == 3:
            p_x, p_y = (x, y)

        if tile == 4:
            b_x, b_y = (x, y)

    # provide input
    if status == 1:
        if b_x != p_x:
            int_comp.programs[0].add_input((b_x - p_x) // abs(b_x - p_x))
        else:
            int_comp.programs[0].add_input(0)

    # reset output
    int_comp.programs[0].reset_output()
