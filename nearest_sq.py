import math


def nearest_sq(n):
    if n == 1:
        return 1
    count = 1
    while n > 1:
        k = math.sqrt(n - count)
        frac, whole = math.modf(k)
        if frac == 0:
            return n - count
        k = math.sqrt(n + count)
        frac, whole = math.modf(k)
        if frac == 0:
            return n + count
        count += 1
