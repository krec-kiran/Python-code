def order(s):
    k = s.split()
    length = len(k)
    result = [0] * length
    for i in range(length):
        test = k[i]
        index = (list(filter(str.isdigit, test))[0])
        result[int(index) - 1] = test
    return(' '.join(result))


s = 'is2 Thi1s T4est 3a'
print(order(s))
