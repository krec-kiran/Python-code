s = '4111111111111111'


def creditCheck(s):
    card = {'AMEX':
            {'start': [34, 37]},
            'Discover':
            {'start': [6011]},
            'Mastercard':
            {'start': [51, 52, 53, 54, 55]},
            'VISA':
            {'start': [4]}
            }

    length = len(s)
    for key, value in card.items():
        if int(s[0]) in value['start'] and (length == 13 or length == 16):
            return(key)
        elif int(s[0:2]) in value['start'] and (length == 15 or length == 16):
            return(key)
        elif int(s[0:4]) in value['start'] and (length == 16):
            return(key)

    return('Unknown')


print(creditCheck(s))
