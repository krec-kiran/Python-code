def pak(string):
    string = string.split()
    text = ''
    for i in range(len(string) - 1):
        text += string[i] + ' ' + 'pak' + ' '
    return(text + string[len(string) - 1])
