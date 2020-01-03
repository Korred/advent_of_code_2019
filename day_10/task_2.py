import math

ast_map = [list(line.strip()) for line in open('task_1_input.txt', 'r').readlines()]
x_len, y_len = len(ast_map[0]), len(ast_map)
vis_map = [[0] * x_len for i in range(y_len)]
sectors = [(1, -1), (1, 1), (-1, 1), (-1, -1)]


def dotproduct(v1, v2):
    return sum((a * b) for a, b in zip(v1, v2))


def length(v):
    return math.sqrt(dotproduct(v, v))


def angle(v1, v2):
    return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))


def on_map(height, width, x, y):
    cond1 = x >= 0 and x < width
    cond2 = y >= 0 and y < height
    return all([cond1, cond2])


x, y = 17, 22

asteroids = set()
for y in range(y_len):
    for x in range(x_len):
        if ast_map[y][x] == "#":
            asteroids.add((x, y))

detectable = {}
for es, s in enumerate(sectors):

    for xm in map(lambda px: px * s[0], range(x_len)):

        for ym in map(lambda py: py * s[1], range(y_len)):
            # print()
            # print(f'x: {x}, y: {y}')
            # print(f'xm: {xm}, ym: {ym}')

            curr_loc = (x + xm, y + ym)
            detec_flag = True

            while True:
                # print(f"loc: {curr_loc}")
                if curr_loc == (x, y) or not on_map(y_len, x_len, curr_loc[0], curr_loc[1]):
                    break

                if curr_loc in detectable:
                    detec_flag = False
                    curr_loc = (curr_loc[0] + xm, curr_loc[1] + ym)
                    continue

                if curr_loc not in detectable:
                    # print(curr_loc, on_map(y_len, x_len, curr_loc[0], curr_loc[1]))
                    if ast_map[curr_loc[1]][curr_loc[0]] == '#':
                        # print(f"visible at {curr_loc}")
                        detectable[curr_loc] = detec_flag
                        detec_flag = False
                    curr_loc = (curr_loc[0] + xm, curr_loc[1] + ym)


detectable = [(key[0] - x, key[1] - y) for key in detectable if detectable[key]]

destroyed = [(math.atan2(dy - y, dx - x), (dx - x, dy - y)) for dx, dy in detectable]

# destroyed.sort(reverse=True)
dx, dy = destroyed[200 - 1][1]
# print(dx, dy)


print("Part 2: {}".format(dy * 100 + dx))

"""

for y, row in enumerate(ast_map):
    for x, loc in enumerate(row):

        if loc == '#':

'''
for row in vis_map:
    print(row)
'''

best_detect_val = max([val for row in vis_map for val in row])

for y, row in enumerate(vis_map):
    x, loc in enumerate(row):
        if loc == best_detect_val:
            print(x,y)

"""
