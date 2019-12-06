orbit_lkp = {}

# read input data
with open('task_1_input.txt', 'r') as data:
    for orbit in data:
        p1, p2 = orbit.strip().split(')')
        orbit_lkp[p2] = p1


def get_path(obj):
    path = []
    while obj in orbit_lkp:
        obj = orbit_lkp[obj]
        path.append(obj)
    return path


orbit_count = sum([len(get_path(obj)) for obj in orbit_lkp])
print(orbit_count)
