raw_data = open('task_1_input.txt', 'r').readlines()

instructions = []
for line in raw_data:
    if 'new' in line:
        instructions.append(('r', None))
        continue

    if 'increment' in line:
        instructions.append(('i', int(line.split()[3])))
        continue

    if 'cut' in line:
        instructions.append(('c', int(line.split()[1])))
        continue

deck = list(range(229))

seen = []
print(deck)
input()

for e, i in enumerate(instructions):

    if i[0] == 'r':
        deck.reverse()

    if i[0] == 'i':
        new_deck = ['0'] * len(deck)
        inc = i[1]
        pos = 0
        for j in range(len(deck)):
            if j == 0:
                new_deck[0] = deck[0]

            elif pos + inc >= len(deck):
                pos = (pos + inc) - len(deck)
                new_deck[pos] = deck[j]
            else:
                pos = pos + inc
                new_deck[pos] = deck[j]

        deck = new_deck

    if i[0] == 'c':
        num = i[1]
        deck = deck[num:] + deck[:num]

    s = tuple(deck)
    if s in seen:
        print(e, "seen")
        print(s)
    else:
        seen.append(s)
