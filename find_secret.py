k = 'This is a test. this test is fun.'


def find_secret_message(paragraph):
    paragraph = paragraph.lower()
    for p in '.,;?!:':
        paragraph = paragraph.replace(p, '')

    paragraph = paragraph.split()
    uniq = []
    dupes = []
    for x in paragraph:
        if x not in uniq:
            uniq.append(x)
        else:
            if x not in dupes:
                dupes.append(x)
    print(uniq)
    print(dupes)
    return(' '.join(dupes))


print(find_secret_message(k))
