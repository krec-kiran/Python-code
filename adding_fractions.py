from functools import reduce
import math


def findgcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def findlcm(a, b):
    lcm = int((a * b) / findgcd(a, b))
    return lcm


def add_fracs(*args):
    l = list(args)
    if not l:
        return('')
    n = [x.split('/') for x in l]
    numerator = [int(x[0]) for x in n]
    denominator = [int(x[1]) for x in n]

    lcm = int(reduce(findlcm, denominator))
    commonD = [(lcm / x) for x in denominator]
    k = []
    j = []

    for i in range(len(commonD)):
        k.append(commonD[i] * numerator[i])
    for i in range(len(commonD)):
        j.append(commonD[i] * denominator[i])

    n_total = 0
    n_total = int(sum(k))
    val = n_total / lcm
    frac, whole = math.modf(val)
    result = 0

    if abs(frac) > 0:
        if n_total % 2 == 0 and lcm % 2 == 0:
            while(n_total % 2 == 0 and lcm % 2 == 0):
                n_total = int(n_total / 2)
                lcm = int(lcm / 2)
        if n_total % 3 == 0 and lcm % 3 == 0:
            while(n_total % 3 == 0 and lcm % 3 == 0):
                n_total = int(n_total / 3)
                lcm = int(lcm / 3)
        if n_total % 5 == 0 and lcm % 5 == 0:
            while(n_total % 5 == 0 and lcm % 5 == 0):
                n_total = int(n_total / 5)
                lcm = int(lcm / 5)
        if n_total % 7 == 0 and lcm % 7 == 0:
            while(n_total % 7 == 0 and lcm % 7 == 0):
                n_total = int(n_total / 7)
                lcm = int(lcm / 7)
        result = str(n_total) + '/' + str(int(lcm))
        return(result)
    else:
        return(str(int(sum(k) / int(lcm))))


print(add_fracs('2/4', '6/4', '4/4'))
