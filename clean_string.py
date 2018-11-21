s = 'abc#d##c'
s = 'abd##c'
# s = 'ab#c'

# s = 'a#b##c'
result = ''
i = 0

if '#' in s:
    print('yes')
else:
    print('no')

while '#' in s:
    while i < (len(s)):
        if i != len(s) - 1 and s[i + 1] == '#':
            i += 2
            result += ''
        else:
            result += s[i]
            i += 1
    print(result)
    if '#' in result:
        s = result
        print(s)
        i = 0
    else:
        print('here', result)
        exit()
