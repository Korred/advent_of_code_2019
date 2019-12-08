from collections import Counter


def join_layers(layers):
    # build layer bottom to top
    joined = layers[-1]

    for layer in layers[:-1][::-1]:
        for e, pixel in enumerate(layer):
            if pixel != '2':
                joined[e] = pixel

    return joined


def print_image(img):
    for row in img:
        print(''.join(row).replace('0', ' '))


pixel_data = list(open('task_1_input.txt', 'r').readline())
w, t = 25, 6
layers = [pixel_data[i * (w * t) : (i + 1) * (w * t)] for i in range(len(pixel_data) // (w * t))]
joined = join_layers(layers)
image = [joined[i * w : (i + 1) * w] for i in range(t)]
print_image(image)
