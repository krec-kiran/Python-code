def apparently(string):
    result = []
    if string == '':
        return ''
    string = string.split()

    for i in range(len(string)):

        if (i == len(string) - 1 or len(string) == 1) and string[i] == 'and':
            result.append('and apparently')

        elif (i == len(string) - 1 or len(string) == 1) and string[i] == 'but':
            result.append('but apparently')

        elif string[i] == 'and' and string[i + 1] != 'apparently':
            result.append('and apparently')

        elif string[i] == 'but' and string[i + 1] != 'apparently':
            result.append('but apparently')
        else:
            result.append(string[i])

    return ' '.join(result)


print(apparently('It was great and I have never been on live television before but sometimes I dont watch this.'))
