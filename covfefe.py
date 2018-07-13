def covfefe(s):
    l = list(s.split())
    result = []
    if 'coverage' not in l:
        return(s + ' ' + 'covfefe')
    for x in l:
        if x == 'coverage':
            x = 'covfefe '
        result.append(x)
    return(''.join(result))


print(covfefe('coverage coverage'))
print(covfefe('nothing'))
