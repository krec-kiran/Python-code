n = 531

from itertools import permutations


def nextSmaller(n):
    l = list(permutations(str(n)))
    k = []
    for i in l:
        k.append(''.join(i))

    k = map(int, k)
    k = sorted(k)
    # print(k)

    val = k.index(n)
    # print("index:", val)

    small = k[val - 1]
    if small < n and len(str(small)) == len(str(n)):
        return(small)
    else:
        return('-1')


print(nextSmaller(1234567908))
print(nextSmaller(29009))
