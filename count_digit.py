'''Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.
Square all numbers k (0 <= k <= n) between 0 and n. Count the numbers of digits d used in
the writing of all the k**2. Call nb_dig (or nbDig or ...)
the function taking n and d as parameters and returning this count.'''


def nb_dig(n, d):
    d = str(d)
    i = 0
    l = [x * x for x in range(n + 1)]
    l = str(l)
    for x in l:
        if d in x:
            i += 1
    return(i)


print(nb_dig(3, 4))
