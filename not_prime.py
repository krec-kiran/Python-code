import math


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def not_primes(a, b):
    p = [2, 3, 5, 7]
    q = [2, 3, 5, 7]
    r = [2, 3, 5, 7]

    l = []
    pq = [int(str(i) + str(j) + str(k)) for i in p for j in q for k in r]
    print(pq)
    l = [x for x in pq if not isPrime(x) and a <= x <= b]
    print(l)


print(not_primes(500, 999))
