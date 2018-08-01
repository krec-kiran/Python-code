def beeramid(bonus, price):
    if bonus < 0:
        return 0

    cans = int(bonus / price)

    total = 0
    i = 0
    while (total <= cans):
        i += 1
        total += i * i

    return(i - 1)
