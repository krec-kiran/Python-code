def next_perfectsq_perm(lower_limit, n):
    from itertools import permutations
    from math import sqrt
    maxsquare = 0
    for i in range(lower_limit + 1, 1000000):
        if sqrt(i) == int(sqrt(i)):
            count = len(str(i))
            k = list((permutations(str(i))))
            k = [x for x in k if '0' not in x]
            l = list(map(int, [''.join(x) for x in k]))
            l = list(set(l))
            s = [x for x in l if sqrt(x) == int(sqrt(x)) and len(
                str(x)) == count]
            s = list(set(s))

            if len(s) == n:
                maxsquare = max(s)
                return(maxsquare)


print(next_perfectsq_perm(100, 4))
