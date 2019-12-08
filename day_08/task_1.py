from collections import Counter

pixel_data = list(open('task_1_input.txt', 'r').readline())
w, t = 25, 6
layers = [Counter(pixel_data[i * (w * t) : (i + 1) * (w * t)]) for i in range(len(pixel_data) // (w * t))]
fewest_0_layer = min(layers, key=lambda x: x['0'])
print(fewest_0_layer['1'] * fewest_0_layer['2'])
