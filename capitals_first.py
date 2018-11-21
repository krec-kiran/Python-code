text = 'sense Does to That Make you?'


def capitals_first(text):
    text = text.split()
    capital = ''
    lower = ''
    for word in text:
        if word[0].isalpha() and not word[0].isdigit():
            if word[0].isupper():
                capital += ' ' + word
            else:
                lower += ' ' + word

    return((capital + lower).strip())


print(capitals_first(text))
