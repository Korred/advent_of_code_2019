import re
import copy
from itertools import permutations

info_pattern = re.compile(r'<x=([-\d]*), y=([-\d]*), z=([-\d]*)>')

data = open('task_1_input.txt', 'r').readlines()
moons = {
    i: dict(zip(['x', 'y', 'z', 'vx', 'vy', 'vz'], list(map(int, info_pattern.search(d).groups())) + [0, 0, 0]))
    for i, d in enumerate(data)
}

# ensure deepcopy of moons object
for i in range(1000000):
    for p in permutations(copy.deepcopy(moons), 2):
        for pos in ['x', 'y', 'z']:
            if moons[p[0]][pos] > moons[p[1]][pos]:
                moons[p[0]]['v' + pos] -= 1
            elif moons[p[0]][pos] < moons[p[1]][pos]:
                moons[p[0]]['v' + pos] += 1

    # update positions
    for moon in moons:
        moons[moon]['x'] += moons[moon]['vx']
        moons[moon]['y'] += moons[moon]['vy']
        moons[moon]['z'] += moons[moon]['vz']

tse = 0
for m in moons.values():
    tse += sum(map(abs, [m['x'], m['y'], m['z']])) * sum(map(abs, [m['vx'], m['vy'], m['vz']]))

print(f'Total System Energy: {tse}')
