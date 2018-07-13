s = 'Cwm fjord bank glyphs vext quiz'
s = s.lower()


def panagram(s):
    l = list(map(chr, range(97, 123)))
    for x in l:
        if x not in s:
            return(False)
    return(True)


print(panagram(s))
