import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def backwardsPrime(start, stop):
    backward = []
    for i in range(start, stop + 1):
        if isPrime(i):
            if i != int(str(i)[::-1]) and isPrime(int(str(i)[::-1])):
                backward.append(i)
    return(backward)


print(backwardsPrime(2, 100))
