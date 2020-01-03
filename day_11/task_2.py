import sys

sys.path.append("..")
from utils.utils import IntComputer, Program

mem = list(map(int, open('task_1_input.txt', 'r').readline().split(',')))

x, y = 0, 0
painted = set()
curr_rot = 'u'  # u - up, d - down, l - left, r - right
rot_lkp = {
    'u': {0: ('l', (-1, 0)), 1: ('r', (1, 0))},
    'd': {0: ('r', (1, 0)), 1: ('l', (-1, 0))},
    'l': {0: ('d', (0, 1)), 1: ('u', (0, -1))},
    'r': {0: ('u', (0, -1)), 1: ('d', (0, 1))},
}
panel_map = [['#']]


int_comp = IntComputer()
int_comp.add_program(Program(mem, [1]))


def adjust_painted(painted, x, y):
    adj = set()
    for pos in painted:
        adj.add((pos[0] + x, pos[1] + y))

    return adj


while int_comp.programs[0].status != 0:
    int_comp.run_prog()
    if int_comp.programs[0].outputs:
        color, rot = int_comp.programs[0].outputs
        color = '.' if color == 0 else '#'

        # clear output
        int_comp.programs[0].reset_output()

        # save color info
        painted.add((x, y))
        panel_map[y][x] = color

        # adjust panel_map
        lkp = rot_lkp[curr_rot][rot]
        curr_rot = lkp[0]
        x, y = x + lkp[1][0], y + lkp[1][1]

        if x < 0:
            for e, row in enumerate(panel_map):
                panel_map[e] = ['.'] + row
            x = 0
            painted = adjust_painted(painted, 1, 0)
        elif x == len(panel_map[0]):
            for e, row in enumerate(panel_map):
                panel_map[e] = panel_map[e] + ['.']

        if y < 0:
            panel_map = [['.'] * len(panel_map[0])] + panel_map
            y = 0
            painted = adjust_painted(painted, 0, 1)
        elif y == len(panel_map):

            panel_map.append(['.'] * len(panel_map[0]))

        inp = 0 if panel_map[y][x] == '.' else 1
        int_comp.programs[0].add_input(inp)


for row in panel_map:
    print("".join(row).replace('.', ' '))
print()

