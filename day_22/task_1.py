raw_data = open('task_1_input.txt', 'r').readlines()

instructions = []
for line in raw_data:
    if 'new' in line:
        instructions.append(('r', None))
        continue

    if 'increment' in line:
        instructions.append(('i', line.split()[3]))
        continue

    if 'cut' in line:
        instructions.append(('c', line.split()[1]))
        continue

deck = list(range(10006))

for i in instructions:
    if i[0] == 'r':
        deck.reverse()
        continue

    if i[0] == 'i':
        new_deck = ['0']*len(deck)
        inc = i[1]
        pos = 0
        for j in range(len(deck)):
            if j == 0:
                new_deck[0] = deck[0]

            elif pos + inc >= len(deck):

            else:
                new_deck[pos+inc] = deck[j]
    


    
    if i[0] == 'c':
        num = i[1]
        deck = deck[num:] + deck[:num] 