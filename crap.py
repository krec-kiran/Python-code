garden = [['_', '_', '_', '_'], ['_', '_', '_', '@'], ['_', '_', '@', '_']]
bags = 2
cap = 2


def crap(garden, bags, cap):
    k = [y for x in garden for y in x]

    if 'D' in k:
        return 'Dog!!'
    if not '@' in k or k.count('@') <= bags * cap:
        return('Clean')
    else:
        return('Cr@p')


print(crap(garden, bags, cap))
