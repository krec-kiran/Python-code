def is_turing_equation(s):
    l = s.split('+')
    numbers = []
    for i in l:
        l = i.split('=')
        numbers.append(l)

    numbers = [x for k in numbers for x in k]
    a = numbers[0]
    b = numbers[1]
    c = numbers[2]
    A = a[::-1]
    B = b[::-1]
    C = c[::-1]

    if int(A) + int(B) == int(C):
        return(True)
    else:
        return(False)


print(is_turing_equation('73+42=16'))
