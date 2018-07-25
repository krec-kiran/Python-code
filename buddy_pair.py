import math


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def perfectCheck(n):
    total = 0
    for p in range(2, int(math.sqrt(n)) + 1):
        if n % p == 0:
            total += p
            pair = int(n / p)
            total += pair
    return total + 1


def buddy(start, limit):
    l = list(range(start, limit))
    l = [x for x in l if not isPrime(x)]

    for n in l:
        total_1 = perfectCheck(n)
        buddy_1 = total_1 - 1
        total_2 = perfectCheck(buddy_1)
        buddy_2 = total_2 - 1
        if buddy_2 == n and start <= n <= limit and buddy_1 > n:
            return[n, buddy_1]
    return('Nothing')


print(buddy(10, 50))
