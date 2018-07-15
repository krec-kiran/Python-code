k = [4, 3, 6, 12, 8, 13, 18, 23]
power = k.pop()
for i in range(len(k), 1, -1):
    base = k.pop()
    print(k, base, power)
