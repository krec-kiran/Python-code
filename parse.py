def parse(data):
    l = []
    i = 0
    for x in data:
        if x is 'i':
            i += 1
        elif x is 'd':
            i -= 1
        elif x is 's':
            i *= i
        elif x is 'o':
            l.append(i)
    return l


print(parse('ioioio'))
