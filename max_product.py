from functools import reduce


def maximum_product(l):
    big = 0
    element = 0
    results = []
    for x in range(1, len(l) + 1):
        values = l[:x - 1] + l[x:]
        prod = reduce((lambda x, y: x * y), values)
        if x == 1 or prod > big:
            big = prod
            element = l[x - 1]
        if x != 1 and prod == big:
            element = l[x - 1]
            results.append(element)
    if not big and len(results) > 1:
        return(min(results))
    else:
        return(element)


print(maximum_product([0, -1, 2, 3]))
print(maximum_product([-1, -2, 0, 1, 2]))
print(maximum_product([-1, 2, -3]))
