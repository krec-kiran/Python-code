def switcheroo(string):
    string = list(string)
    i = 0
    while i < len(string):
        if string[i] == 'a':
            string[i] = 'b'
            i += 1
        elif string[i] == 'b':
            string[i] = 'a'
            i += 1
        else:
            i += 1
    return(''.join(string))


print(switcheroo('abcabcbaac'))
