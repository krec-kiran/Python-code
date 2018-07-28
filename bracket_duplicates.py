k = 'aaaabbcdefffffffg'


def string_parse(k):
    uniq = []
    l = []
    result = []
    for i in k:
        if i not in uniq:
            uniq.append(i)
    for i in uniq:
        l.append(k.count(i))
    z = list(zip(uniq, l))
    result = [[x[0]] * x[1] for x in z]
    final = []
    for x in result:
        if len(x) > 2:
            value = x.pop() + x.pop()
            extras = ''.join(x)
            value = value + '[' + extras + ']'
            final.append(value)
        else:
            final.append(''.join(x))

    return(''.join(final))


print(string_parse(k))
