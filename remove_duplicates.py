s = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
s = list(s.split())
result = list()
for x in s:
    if x not in result:
        result.append(x)
print(' '.join(result))
