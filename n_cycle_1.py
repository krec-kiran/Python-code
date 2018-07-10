def cycle(n):
    if n % 5 == 0 or n % 2 == 0:
        return(-1)
    l = list()
    for i in range(1, 10000):
        if pow(10, i) > n:
            l.append(pow(10, i))
    for p in l:
        if (p % n) == 1:
            return(str(p).count('0'))


print(cycle(38127))
