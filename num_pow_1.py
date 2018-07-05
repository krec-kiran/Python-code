def power_sumDigTerm(index):
    l = []
    r = 2
    for n in range(10, 100000000):
        s = list(map(int, str(n)))
        for r in range(2, 5):
            if pow(sum(s), r) == n:
                l.append(n)
    print(l)
    if index <= len(l):
        return(l[index - 1])


print(power_sumDigTerm(12))
