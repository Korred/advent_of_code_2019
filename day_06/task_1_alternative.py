orbit_lkp = {}

# read input data
with open('task_1_input.txt', 'r') as data:
    for orbit in data:
        p1, p2 = orbit.strip().split(')')
        orbit_lkp[p2] = p1


# find endpoints
# objects that do not have other objects on orbit around them
no_objects_around = set(orbit_lkp.keys()) - set(orbit_lkp.values())

# orbit count lookup
orbit_count = {}


def count_connections(obj):
    if obj in orbit_count:
        return orbit_count[obj]

    else:
        if obj in orbit_lkp:
            orbit_count[obj] = 1 + count_connections(orbit_lkp[obj])
            return orbit_count[obj]
        else:
            return 0


for obj in no_objects_around:
    count_connections(obj)

print(sum(orbit_count.values()))
