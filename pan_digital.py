k = set()
start = {1, 2, 3, 4, 5, 6, 7, 8, 9}
l = start
i = 0
big = 0
for i in range(2, 500):
    for j in l:
        val = i * j
        p = set(map(int, set(str(val))))
        if (k & p):
            l = start
            k = set()
            break
        k.update(p)
        if k == start:
            print("Number %d is pandigital" % i)
            if i > big:
                big = i
            l = start
            # exit()
        else:
            l = (l - p)
        # print(l, k, p
print("Biggest pandigital so far", big)
