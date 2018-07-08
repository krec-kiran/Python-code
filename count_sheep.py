def count_sheep(n):
    murmur = ''
    for i in range(1, n + 1):
        murmur += str(i) + ' sheep...'
    return(murmur)


print(count_sheep(3))
