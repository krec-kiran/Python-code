k = [3, 2, 6, 2, 1, 3]


def group(arr):
    uniq = []
    l = []
    result = []
    for i in arr:
        if i not in uniq:
            uniq.append(i)
    for i in uniq:
        l.append(k.count(i))
    z = list(zip(uniq, l))
    result = [[x[0]] * x[1] for x in z]
    return(result)


print(group(k))
