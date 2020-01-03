import re
from math import gcd


def least_common_multiple(x, y):
    return x // gcd(x, y) * y


def find_circle(axis_pos):
    print(axis_pos)
    v = [0] * len(axis_pos)
    target_pos = tuple(axis_pos) + tuple(v)
    steps = 0
    while True:
        for m1 in range(len(axis_pos)):
            for m2 in range(m1 + 1, len(axis_pos)):
                if axis_pos[m1] < axis_pos[m2]:
                    v[m1] += 1
                    v[m2] -= 1
                elif axis_pos[m1] > axis_pos[m2]:
                    v[m1] -= 1
                    v[m2] += 1

        for m, _ in enumerate(axis_pos):
            axis_pos[m] += v[m]

        steps += 1
        curr_pos = tuple(axis_pos) + tuple(v)
        if curr_pos == target_pos:
            return steps


info_pattern = re.compile(r'<x=([-\d]*), y=([-\d]*), z=([-\d]*)>')
data = open('task_1_input.txt', 'r').readlines()
moons = [list(map(int, info_pattern.search(d).groups())) for d in data]

steps_x = find_circle([m[0] for m in moons])
steps_y = find_circle([m[1] for m in moons])
steps_z = find_circle([m[2] for m in moons])

print(steps_x, steps_y, steps_z)

cycle = least_common_multiple(steps_x, least_common_multiple(steps_y, steps_z))

print(cycle)
