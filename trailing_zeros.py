number = 50


def trailerZeros(number):
    factorial = 1
    trailer = 0
    for i in range(1, number + 1):
        factorial *= i
    print(factorial)
    factorial = str(factorial)
    while(factorial[-1:] == '0'):
        trailer += 1
        factorial = factorial[:-1]
        # print(factorial)

    return(trailer)


print(trailerZeros(50))
