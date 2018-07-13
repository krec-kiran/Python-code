d = '$1.00'

d = d[1:]
d = d.split('.')


def dollar(d):
    d = d[1:]
    d = d.split('.')
    if d[0] == '1' and d[1] == '00':
        message = d[0] + ' dollar'
        return message
    elif len(d) == 1 or d[1] == '00':
        message = d[0] + ' dollars'
        return message
    else:
        message = d[0] + ' dollars and ' + d[1] + " cents"
        return message


print(dollar('$10.20'))
