def binary_pyramid(m, n):
    result = 0
    for k in range(m, n + 1):
        result += int(bin(k).replace('0b', ''))
    return(str(bin(result).replace('0b', '')))


print(binary_pyramid(1, 4))
