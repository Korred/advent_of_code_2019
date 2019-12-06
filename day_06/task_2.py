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


you_orbits = get_path('YOU')
santa_orbits = get_path('SAN')

for p in you_orbits:
    if p in santa_orbits:
        transfers = sum([you_orbits.index(p), santa_orbits.index(p)])
        print(f"Minimum number of orbital transfers: {transfers}")
        break
