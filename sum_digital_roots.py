n = 1423982
s = list(str(n))
k = list(map(int, s))
while len(k) > 1:
    k = sum(k)
    s = list(str(k))
    k = list(map(int, s))
print(k[0])
