n = -420902


def number_format(n):
    l = list(str(n))
    i = len(l) - 1
    k = 0
    while i > 0:
        k += 1
        if k % 3 == 0 and l[i - 1] != '-':
            l.insert(i, ',')
        i -= 1
    return ''.join(l)


print(number_format(n))
