number = 12345


def digits(number):
    number = list(str(number))
    k = []
    for i in range(len(number)):
        current = int(number[i])
        rest = number[i + 1:]
        k.append([current + int(x) for x in rest])
    result = [x for p in k for x in p]
    return(result)


print(digits(number))
