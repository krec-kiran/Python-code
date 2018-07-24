import math


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def odd_not_prime(n):
    count = 0
    l = [x for x in range(1, n + 1) if x % 2 != 0]
    for i in l:
        if not isPrime(i):
            count += 1
    return(count)


print(odd_not_prime(9495))
