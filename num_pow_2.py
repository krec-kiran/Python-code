def power_sumDigTerm(index):
    l = set()
    for n in range(2, 100):
        for p in range(2, 15):
            k = pow(n, p)
            l.add(k)
    l = sorted(l)
    # print(l)

    b = set()
    for x in l:
        s = list(map(int, str(x)))
        for p in range(2, 63):
            if pow(sum(s), p) == x:
                b.add(x)
    b = list(sorted(b))
    print(b)
    return(b[index - 1])


print(power_sumDigTerm(5))
