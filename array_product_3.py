# Use filter to filter out a specific element..
from functools import reduce
n = [1, 2, 3, 4, 2, 4]
product = [0] * len(n)

for i in range(len(n)):
    k = n.pop(0)
    print(n)
    if 0 not in n:
        result = reduce((lambda x, y: x * y), n)
        product[i] = result
    n.append(k)
print(product)
