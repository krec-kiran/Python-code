# Use dictionary to reduce time complexity
from functools import reduce
n = [1, 2, 3, 4, 9, -3, 3]
product = [0] * len(n)
d = dict()
for i in range(len(n)):
    k = n.pop(0)
    if k in d.keys():
        product[i] = d[k]
    elif 0 not in n:
        result = reduce((lambda x, y: x * y), n)
        product[i] = result
        d[k] = result
    n.append(k)
print(product)
