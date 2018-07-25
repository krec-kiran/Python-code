import math
from itertools import product


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def not_primes(a, b):
    p = [2, 3, 5, 7]
    l = []
    k = []
    freq = len(str(b))
    index = 2
    while index <= freq:
        l = [p for p in product(p, repeat=index)]
        if index == 2:
            l = [int(''.join(str(x) + str(y))) for x, y in l]
            k = k + l
        if index == 3:
            l = [int(''.join(str(x) + str(y) + str(z))) for x, y, z in l]
            k = k + l
        if index == 4:
            l = [int(''.join(str(x) + str(y) + str(z) + str(w)))
                 for x, y, z, w in l]
            k = k + l
        if index == 5:
            l = [int(''.join(str(x) + str(y) + str(z) + str(w) + str(p)))
                 for x, y, z, w, p in l]
            k = k + l
        index += 1
    l = [x for x in k if a <= x < b]
    l = [x for x in l if not isPrime(x)]
    return(l)


print(not_primes(2700, 3000))
