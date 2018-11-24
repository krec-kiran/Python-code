def ap(a, r, n):
    sum = a
    for i in range(1, n):
        sum += a + (r * i)
    return sum


print(ap(2, 3, 5))
