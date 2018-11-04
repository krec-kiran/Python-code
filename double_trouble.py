def trouble(x, t):
    i = 0
    while (i < len(x) - 1):
        if x[i] + x[i + 1] == t:
            x.pop(i + 1)
            i = 0
        else:
            i += 1
    return(x)


print(trouble([1, 3, 5, 6, 7, 4, 3], 7))
