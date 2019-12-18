import sys

sys.path.append("..")
from utils.utils import IntComputer, Program

mem = list(map(int, open('task_1_input.txt', 'r').readline().split(',')))

int_comp = IntComputer()
int_comp.add_program(Program(mem, []))

while int_comp.programs[0].status != 0:
    int_comp.run_prog()

output = int_comp.programs[0].outputs
draw_instructions = [output[i : i + 3] for i in range(0, len(output), 3)]

block_tiles = set()

for i in draw_instructions:
    x, y, tile = i

    if tile == 0:
        try:
            block_tiles.remove((x, y))
        except KeyError:
            pass

    if tile == 2:
        block_tiles.add((x, y))


print(len(block_tiles))
