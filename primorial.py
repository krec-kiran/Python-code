from functools import reduce


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def num_primorial(n):
    l = []
    i = 0
    prime = 2
    while i < n:
        if isPrime(prime):
            l.append(prime)
            i += 1
        prime += 1

    prod = reduce((lambda x, y: x * y), l)
    return prod
