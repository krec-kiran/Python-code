import math


def isPrime(n):
    if n < 2:
        return False
    for t in range(2, int(math.sqrt(n))):
        if n % t == 0:
            return False
    return True


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def am_i_wilson(n):
    if isPrime(n):
        print(n, 'is prime')
        val = (math.factorial(n - 1) + 1) % (n * n)
        if val == 0:
            return True
        else:
            return False
    else:
        return False


print(am_i_wilson(563))
print(am_i_wilson(11))
print(am_i_wilson(5))
