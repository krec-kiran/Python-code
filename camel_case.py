def to_camel_case(text):
    if text == '':
        return ''
    for x in '_-':
        text = text.replace(x, ' ')
    l = text.split()

    for i in range(1, len(l)):
        l[i] = l[i].capitalize()

    return(''.join(l))


print(to_camel_case('the_stealth - warrior'))
