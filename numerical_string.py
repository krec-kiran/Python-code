s = 'Hello, World!'
result = ''
d = dict()

for i in s:
    if not i in d.keys():
        d.update({i: 1})
    else:
        d[i] = d[i] + 1
    result += str(d[i])

print(result)
