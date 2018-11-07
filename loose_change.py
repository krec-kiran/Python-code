def loose_change(cents):
    d = dict({'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
    if cents <= 0:
        return d
    while cents > 0:
        cents = int(cents)
        if cents >= 25:
            d['Quarters'] = int(cents / 25)
            cents = cents % 25
        if cents >= 10 and cents < 25:
            d['Dimes'] = int(cents / 10)
            cents = cents % 10
        if cents >= 5 and cents < 10:
            d['Nickels'] = int(cents / 5)
            cents = cents % 5
        if cents >= 1 and cents < 5:
            d['Pennies'] = int(cents / 1)
            cents = cents % 1
    return d


print(loose_change(91))
print(loose_change(29))
print(loose_change(198))
