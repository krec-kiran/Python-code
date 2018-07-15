from itertools import permutations


def next_smaller(n):
    s = str(n)
    l = []
    l = list(permutations(s))
    l = list(set([''.join(x) for x in l]))
    l = list(map(int, l))
    l = sorted(l)
    index = l.index(n)
    if index:
        return l[index - 1]
    else:
        return(-1)


print(next_smaller(414))
