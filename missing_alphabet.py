s = 'hello'
l = list(map(chr, range(97, 123)))
result = ''
missing = ''
for x in s:
    index = l.index(x)
    after = ''.join(l[index + 1:])
    after = [x for x in after if x not in s]
    after = ''.join(after).upper()
    if x not in result:
        missing = x + after
    else:
        missing = x
    result += missing
    print("String", result)
