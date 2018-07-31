def add(*args):
    l = list(args)
    print(l)
    sum = 0
    for i in range(len(l)):
        sum += i
    return sum


print(add(1, 2, 3))
print(add(1, 2, 3, 4, 5))
print(add(1))
