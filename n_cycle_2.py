
n = 69


def cycle(n):
    if n % 5 == 0 or n % 2 == 0:
        return(-1)
    k = 0
    i = 0
    while(k < n):
        i += 1
        k = pow(10, i)
    print("i is", i)
    p = 1
    for p in range(i, 1000):
        ans = (pow(10, p) % n)
        if ans == 1:
            return(p)


print(cycle(69))
