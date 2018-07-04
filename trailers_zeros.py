def zeros(number):
    count = 0
    for x in range(5, number + 1, 5):
        while x % 5 == 0:
            count += 1
            x = x / 5
    return(count)


print(zeros(100))
