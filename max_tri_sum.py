l = [3, 2, 6, 8, 2, 3]
s = set(l)
s = sorted(s, reverse=True)
s = list(s)
print(s)
toto = 0
for i in range(3):
    toto += s[i]
print(toto)
print(s)
