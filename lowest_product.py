from functools import reduce


def lowest_product(input):
    n = [int(x) for x in str(input)]
    if len(n) < 4:
        return "Number is too small"
    start = 0
    small = prod = reduce((lambda x, y: x * y), n)

    while start <= len(n) - 4:
        prod = reduce((lambda x, y: x * y), n[start:start + 4])
        if prod < small:
            small = prod
        start += 1
    return(small)


print(lowest_product(123456789))
