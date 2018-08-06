toto = 10
digits = 3

l = [1] * 3
print("initial", l)


k = []
index = 0
for i in range(27):
    if sum(l) == 10:
        k.append(l)
    l[index] += 1
    if l[index] > 9:
        l[index] = 1
        index = index + 1
    print(l)
    # print(k)
