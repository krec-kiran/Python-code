test = [18, -4, 7, 12, -9]


def returnPositive(test):
    sum = 0
    if len(test) == 0:
        return 0
    for i in range(len(test)):
        if test[i] > 0:
            sum += test[i]
    return sum


print(returnPositive(test))
