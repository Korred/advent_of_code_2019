wires = []

# read input data
with open('task_1_input.txt', 'r') as data:
    for line in data:
        wires.append(line.split(','))


central_point = (0, 0)
lines = []

# calculate all lines first
for e, wire in enumerate(wires):
    current_point = (0, 0)
    lines.append([])
    for path in wire:
        direction = path[0]
        steps = int(path[1:])

        sp = current_point

        if direction == 'R':
            current_point = (sp[0] + steps, sp[1])

        elif direction == 'L':
            current_point = (sp[0] - steps, sp[1])

        elif direction == 'U':
            current_point = (sp[0], sp[1] + steps)

        elif direction == 'D':
            current_point = (sp[0], sp[1] - steps)

        lines[e].append((sp, current_point))

# https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
def findIntersection(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    det = ((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4))

    if det == 0:
        return (False, None)

    else:
        # calculates intersection of lines
        # requires additional check for line segments

        dx = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / det
        dy = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / det

        # print(dx, dy)

        c1 = min(x1, x2) <= dx
        c2 = dx <= max(x1, x2)
        c3 = min(x3, x4) <= dx
        c4 = dx <= max(x3, x4)
        c5 = min(y1, y2) <= dy
        c6 = dy <= max(y1, y2)
        c7 = min(y3, y4) <= dy
        c8 = dy <= max(y3, y4)

        if all([c1, c2, c3, c4, c5, c6, c7, c8]):
            return (True, (dx, dy))
        else:
            return (False, None)


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


# find intersections
intersections = []

for e, g1 in enumerate(lines):
    for line1 in g1:

        for g2 in lines[e + 1 :]:
            for line2 in g2:

                intersection = findIntersection(line1, line2)
                if intersection[0]:
                    intersections.append(intersection[1])


# find min distance to central_point
min_intersection = min(intersections, key=lambda x: manhattan_distance(x, central_point))
print(manhattan_distance(min_intersection, central_point))
