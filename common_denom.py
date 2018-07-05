def findGCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def commonDenom(n):
    numbers = [x[1] for x in n]
    i = 0
    start = numbers[0]
    while i < len(numbers) - 1:
        lcm = int((start * numbers[i + 1]) / findGCD(start, numbers[i + 1]))
        i += 1
        start = lcm

    l = []
    i = 0
    for x in numbers:
        val = int(lcm / x)
        element = [n[i][0] * val, n[i][1] * val]
        l.append(element)
        i += 1
    return(l)


n = [[1, 2], [1, 3], [1, 4]]
print(commonDenom(n))
