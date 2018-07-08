# Use filter to filter out a specific element..
from functools import reduce
n = [1, 2, 3, 4]
product = [None] * len(n)
for i in range(len(n)):
    l = [x for x in n if x != n[i]]
    result = reduce((lambda x, y: x * y), l)
    product[i] = result
print(product)
