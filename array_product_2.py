from functools import reduce
# n = [1, 2, 3, 4, 0, 0]
n = [6, 1, -3, 3, 7, 3, 3, 4, 5, 6, -4, 1, 6, 7, 3, -7, 5, 6, 7, 1, 2, 6, 4, 4, 6, 2, -2, 6, 2, 2, 6, -2, 5, 4, -5, 1, 2, 3, -2, -4, 6, 1, -6, 6, 1, -7, 2, 6, 2, 1, 5, 1, 5, 7, 1, 3, -3, 4, -3, 4, 3, 1, -5, 1, 4, 5, -5, -2, -5,
     7, 1, 3, 6, 1, -4, 7, -7, 7, 7, 1, 4, -2, 7, -2, 5, -4, 2, 2, 1, 3, -4, 2, 4, 2, 2, 6, 7, -3, -1, 7, -1, -6, 6, -2, 6, 2, 4, -4, 3, -2, 3, 6, -3, -1, 6, 5, 6, 7, -7, -2, 5, -3, -1, 6, 3, 4, 2, 4, -4, 7, 2, -7, 7, 1, 2, -6]

k = list(n)
result = 0
print(n)
value = 0
product = [0] * len(n)
print(result)
for i in range(len(n)):
    if n.count(0) == 1:
        index = n.index(0)
        n.remove(0)
        result = reduce((lambda x, y: x * y), n)
        product[index] = result
    elif n.count(0) == 0:
        result = reduce((lambda x, y: x * y), n)
        product[i] = int(result / n[i])

    n = list(k)
print(product)
