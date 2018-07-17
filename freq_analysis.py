def bucketize(*arr):
    arr = list(arr)
    result = [None] * (len(arr) + 1)
    d = dict()
    for i in arr:
        f = arr.count(i)
        if f in d.keys():
            d[f].append(i)
        else:
            d[f] = [i]

    for i in range(len(arr) + 1):
        if i in d.keys():
            result[i] = sorted(list(set(d[i])))

    return result


print(bucketize(2, 2, 4, 4, 6, 6, 9, 9, 9, 9))
