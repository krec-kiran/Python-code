#
# result = [x ** y for x in [10, 20, 30] for y in [2, 3, 4]]
# print(result)

from functools import reduce

result = reduce((lambda x, y: x * y), [1, 2, 3])
print(result)
