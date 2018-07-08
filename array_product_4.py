# Use filter to filter out a specific element..
from functools import reduce
n = n = [1, 2, 3, 4, 2, 4]
k = list(n)
product = [0] * len(n)
result = 0
zero_sum = 0
if k.count(0) < 1:
    result = reduce((lambda x, y: x * y), k)
elif k.count(0) == 1:
    k.remove(0)
    zero_sum = reduce((lambda x, y: x * y), k)
    print("Result", result)
# print("K", k)
# print("n", n)

for i in range(len(n)):
    k = n.pop(0)
    print(n)
    if k == 0:
        product[i] = zero_sum
    if k != 0 and 0 not in n:
        product[i] = int(result / k)
        n.append(k)
print(product)
