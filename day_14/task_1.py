from collections import deque

react_lkp = {}
for r in list(open('task_1_input.txt').readlines()):
    left, right = r.split(' => ')
    right_output = right.split()

    react_lkp[right_output[1]] = {
        'depth': None,
        'amt': int(right_output[0]),
        'inputs': [],
    }

    left_inputs = left.split(', ')
    for inp in left_inputs:
        dat = inp.split()
        react_lkp[right_output[1]]['inputs'].append((int(dat[0]), dat[1]))


def gen_order(root):
    q = deque()
    # init with root info
    q.append((root, 0))

    while q:
        chem, depth = q.popleft()
        react_lkp[chem]['depth'] = depth
        for _, inp in react_lkp[chem]['inputs']:
            if inp != 'ORE':
                q.append((inp, depth + 1))


def ore_needed(amt, root):
    resolved = {}
    ore_needed = 0
    q = deque()
    q.append((amt, root, 0))

    while q:
        # order by height
        q = deque(sorted(q, key=lambda x: x[2]))

        amt, chem, depth = q.popleft()

        if amt <= react_lkp[chem]['amt']:
            mul = 1
        elif amt > react_lkp[chem]['amt']:
            mul = 1
            while amt > (react_lkp[chem]['amt'] * mul):
                mul += 1

        for a, inp in react_lkp[chem]['inputs']:
            if inp == 'ORE':
                ore_needed += a * mul
                break

            else:
                joined = False
                for e, entry in enumerate(q):
                    if entry[1] == inp:
                        q[e] = ((a * mul) + entry[0], inp, entry[2])
                        joined = True
                        break

                if not joined:
                    q.append((a * mul, inp, react_lkp[inp]['depth']))

    return ore_needed


# gen ordered tree
gen_order('FUEL')

'''
for k in react_lkp:
    print(k, react_lkp[k])
    print()
'''

print(ore_needed(1, 'FUEL'))

