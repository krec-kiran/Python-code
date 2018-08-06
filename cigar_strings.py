import re


def is_matched(read):
    match, base = read
    s = match
    index = match.find('M')
    match = match[:index]

    l = (re.findall('\d+', s))
    total = sum([int(x) for x in l])

    if total != len(base):
        return('Invalid cigar')
    if 'M' in s and len(base) == int(match):
        return(True)
    elif 'M' not in s or int(match) < len(base) and len(base) != int(match):
        return(False)


print(is_matched(('36M', 'ACTCTTCTTGCGAAAGTTCGGTTAGTAAAGGGGATG')))
print(is_matched(('20M10S', 'ACTCTTCTTGCGAAAGTTCGGTTAGTAAAG')))
