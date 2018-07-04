def pig_it(s):
    s = s.split()
    result = ""
    for k in s:
        if(k.isalpha()):
            k = k[1:] + k[0] + 'ay'
        result += k + ' '
    return result


print(pig_it('Pig latin , is cool'))
