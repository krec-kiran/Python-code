def isPrime(n):
    n = int(n)
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def circular_prime(n):
    n = str(n)
    l = []
    l.append(n)
    c = n
    for i in range(len(n) - 1):
        c = c[1:] + c[0]
        l.append(c)

    for i in l:
        if not isPrime(i):
            return False
    return True


print(circular_prime(1917))
