# Use filter to filter out a specific element..
from functools import reduce
n = [1, 2, 3, 4]
product = [0] * len(n)
for k in range(len(n)):
    l = [i for i in range(len(n)) if i != k]
    # print(l)
    p = [n[x] for x in l]
    print(p)
    product[k] = reduce((lambda x, y: x * y), p)
print(product)
