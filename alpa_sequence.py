def alpha_seq(string):
    string = string.upper()
    string = sorted(string)
    string = ''.join(string).lower()

    text = ''
    for i in string:
        text += i.upper() + i.lower() * ((ord(i.lower()) - 97)) + ','

    text = text.strip(',')
    return(text)
