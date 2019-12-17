from itertools import cycle
from collections import deque

signal = list(map(int, open('task_1_input.txt', 'r').readline()))


def parse_signal(signal, phases):
    for phase in range(phases):
        left_half = []
        b = 1
        for e, s in enumerate(signal[: (len(signal) // 2)]):

            rel = [
                sum(signal[i : i + b]) if n % 2 == 0 else sum(signal[i : i + b]) * -1
                for n, i in enumerate(range(e, len(signal), 2 * b))
            ]
            b += 1

            su = abs(sum(rel)) % 10
            left_half.append(su)

        right_half = deque()
        right_half.append(signal[-1])

        i = -1
        for s in reversed(signal[(len(signal) // 2) : -1]):
            nv = abs(s + right_half[i]) % 10
            right_half.appendleft(nv)
            i -= 1

        signal = left_half + list(right_half)

    return signal[:8]


result = parse_signal(signal, 100)
print(result)

