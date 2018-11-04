def findGCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a


print(findGCD(24, 45))
print(findGCD(36, 81))
