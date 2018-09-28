string = 'abracadabra'


def solve(string, count):
    if count > len(string):
        return ''
    k = 97
    while count > 0:
        l = chr(k)
        if l in string:
            letter_count = string.count(l)
            string = string.replace(l, '', count)
            count -= letter_count
        if count > 0:
            k += 1
    return string


print(solve(string, 8))
