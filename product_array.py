numbers = [1, 2, 3, 4, 5]

from functools import reduce


def product_array(numbers):
    result = []
    for x in range(0, len(numbers)):
        k = numbers[:x] + numbers[x + 1:]
        print(k)
        product = reduce(lambda x, y: x * y, k)
        result.append(product)
    return result


print(product_array(numbers))
