a = [7, 1, 12, 9, 11, 14, 13, 6, 10, 5]


def miss_nums_finder(a):
    b = [1] * (max(a) + 1)
    for i in range(1, max(a) + 1):
        b[i] = i

    c = list(set(b) - set(a))
    return(sorted(c))


print(miss_nums_finder(a))
