s = 'aba'


def count(string):
    d = dict()
    for i in string:
        d[i] = string.count(i)
    return d


print(count(s))
