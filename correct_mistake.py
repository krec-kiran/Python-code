def correct(string):
    d = {'5': 'S', '0': 'O', '1': 'I'}
    result = ''
    for x in string:
        if x in d.keys():
            string = string.replace(x, d[x])
    return(string)


print(correct('51NGAP0RE'))
