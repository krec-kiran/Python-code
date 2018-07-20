def digitroot(k):
    k = str(k)
    k = list(map(int, list(k)))
    return(sum(k))


def deeperSquare(k):
    k = str(k)
    k = list(map(int, list(k)))
    product = 0
    for i in k:
        product += i * i
    return(product)


def sorted_comm_by_digs(arr1, arr2):
    l = list(set(arr1) & set(arr2))
    d = dict()
    result = []
    for x in l:
        dr = digitroot(x)
        dsaddr = deeperSquare(dr)
        total = dr + dsaddr
        result.append(total)
        if total in d.keys():
            d[total].append(x)
        else:
            d[total] = [x]
    b = []

# First sort the lists within dictionary in ascending order
    for k in d:
        d[k].sort()

# Second, sort the dictionary by keys which are the total deep roots -
    s = sorted(d.keys(), reverse=True)

# Third append the original numbers / values of those keys obtained above
    for x in s:
        b.append(d[x])

# Fourth - append the lists within list creating one final list
    b = [p for x in b for p in x]
    return(b)
