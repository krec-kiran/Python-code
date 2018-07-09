s = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
s = list(s.split())
# print(''.join(set(list(s.split()))))
print(s)
result = list()

for x in s:
    if x not in result:
        result.append(x)
print(' '.join(result))
