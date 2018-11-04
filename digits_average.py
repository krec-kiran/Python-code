import math


def digits_average(input):
    avg = []
    k = [int(x) for x in str(input)]
    while len(k) != 1:
        for i in range(len(k) - 1):
            mean = math.ceil((k[i] + k[i + 1]) / 2)
            avg.append(mean)
        k = avg
        avg = []
    return(k[0])


print(digits_average(2468))
