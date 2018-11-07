items = [12, 14, 63, 72, 55, 24]
a = 2
b = 4


def inverse_slice(items, a, b):
    return items[:a] + items[b:]


print(inverse_slice(items, a, b))
