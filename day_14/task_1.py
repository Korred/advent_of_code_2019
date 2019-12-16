from collections import deque

react_lkp = {} 
for r in list(open('test_input_2.txt').readlines()):
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

    print(q)
    print()

    while q:
        chem, depth = q.popleft()
        react_lkp[chem]['depth'] = depth
        for _, inp in react_lkp[chem]['inputs']:
            if inp != 'ORE':
                q.append((inp, depth+1))

        print(q)
        print()
        for chem in react_lkp:
            print(chem, react_lkp[chem])
        input()    

def ore_needed(amt, root):
    resolved = {}
    q = deque()
    q.append((amt, root, 0))

    while q:
        amt, chem, depth = q.popleft()
        for a, inp in react_lkp[chem]['inputs']:
            if inp == 'ORE':          
                if inp in resolved:
                    resolved[inp] = amt
                else:
                    resolved[inp] += amt
            
            else:
                mul

                val = * a
                q.append((val, inp, react_lkp[chem]['depth']))


# gen ordered tree
gen_order('FUEL')





"""


def get_req_ore_for(amt, chem, mul=1):
    if chem == 'ORE':
        return amt
    else:

        # check if there is enough chem already available before producing
        if produced[chem] >= amt:
            produced[chem] -= amt
            return 0
        else:
            amt -= produced[chem]
            produced[chem] = 0

        # not enough prodcut available - produce new chems
        chem_reaction = react_lkp[chem]

        # find multiplier
        multiplier = 1
        if amt < chem_reaction['amt']:
            # retain overproduced chems
            produced[chem] += chem_reaction['amt'] - amt
        elif amt > chem_reaction['amt']:
            while (multiplier * chem_reaction['amt']) < amt:
                multiplier += 1

        ore_amt = 0
        for inp in chem_reaction['inputs']:
            print(inp)
            ore_amt += get_req_ore_for(multiplier*inp[0], inp[1])

        return ore_amt

print(get_req_ore_for(1, 'FUEL'))


"""    