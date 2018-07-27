arr = [["white", "goodness"], ["blue", "tranquility"]]


def colour_association(arr):
    l = []
    for i in arr:
        d = dict()
        d[i[0]] = i[1]
        l.append(d)
    return(l)


print(colour_association(arr))
# [{'white': "goodness"}, {'blue': "tranquility"}]
