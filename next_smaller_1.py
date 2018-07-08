from itertools import permutations


def nextSmaller(n):
    l = list(str(n))
    for i in range(2, len(l) + 1):
        first = l[:-i]
        last = l[-i:]
        t = ''.join(last)
        k = list(permutations(last))
        b = []
        for i in k:
            b.append(''.join(i))
        small = 0
        for x in sorted(b):
            if x < t:
                small = x
        if small != 0 and small < t:
            final = ''.join(first) + str(small)
            if final[:1] != '0':
                return(int(''.join(final)))
            else:
                return(-1)

    return(-1)


print(nextSmaller(907))
print(nextSmaller(29009))
# print(nextSmaller(120235849778909360000122334567788999))
# print(nextSmaller(123456798))
