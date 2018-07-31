text = "The sunset sets at twelve o' clock."


def alphabet_position(text):
    if text.isdigit():
        return ''
    l = list(map(chr, range(97, 123)))
    d = dict(enumerate(l, 1))
    res = dict((v, k) for k, v in d.items())
    text = text.lower()
    text = text.replace(" ", "")
    for i in "'.":
        text = text.replace(i, "")
    for i in text:
        if i.isalpha():
            text = text.replace(i, str(res[i]) + ' ')
    text = text.strip()
    return text


print(alphabet_position(text))
