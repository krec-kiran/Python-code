def thirt(number):
    l = [1, 10, 9, 12, 3, 4]
    toto = 0
    while number != toto:
        n = [int(x) for x in str(number)[::-1]]
        j = 0
        for i in n:
            toto += i * l[j]
            if j == len(l) - 1:
                j = -1
            j += 1
        if number != toto:
            number = toto
            toto = 0
        else:
            break
    return(number)


print(thirt(1234567))
print(thirt(167))
print(thirt(18945))
