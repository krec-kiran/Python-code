import math


def movie(card, ticket, perc):
    val = 0
    i = 0
    sys_a = 0
    sys_b = 0
    while sys_a <= math.ceil(card + sys_b):
        i += 1
        val = ticket * math.pow(perc, i)
        sys_b += val
        sys_a = ticket * i
    return(i)


print(movie(500, 15, 0.9))
print(movie(100, 10, 0.95))
