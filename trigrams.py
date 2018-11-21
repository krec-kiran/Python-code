phrase = 'the quick red'


def trigrams(phrase):
    result = ''
    start = 0
    for i in range(len(phrase) - 2):
        result += ' ' + phrase[start:start + 3].replace(' ', '_')
        start += 1

    return(result.strip())


print(trigrams(phrase))
