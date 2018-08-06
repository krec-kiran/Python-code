# optimize
def find_x(n):
    k = n * 2
    partial = sum(range(n))
    total = partial * 2 + (n * n)
    toto = total * n
    small = partial * k
    return toto + small


print(find_x(2))
print(find_x(3))
print(find_x(4))
print(find_x(5))
