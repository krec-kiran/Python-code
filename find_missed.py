s = '2198765123416171890101112131415'
k = list(map(int, list(s)))
print(k)
#
for i in range(1, 22):
    print('i', i)
    if i < 10:
        if i in k:
            k.remove(i)
            print(k)
    else:
        k =
