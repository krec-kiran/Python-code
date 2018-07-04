def zeros(number):
    count = 0
    factor = 1
    if (number % 5) != 0:
        number = number - (number % 5)
    divider = 1
    while(divider < number):
        divider = pow(5, factor)
        print(divider)
        count += number / (divider)
        factor += 1
    return(int(count))


print(zeros(1000000000))
