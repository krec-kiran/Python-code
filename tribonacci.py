def tribonacci(signature, n):
    if n < 3:
        return signature[:n]
    counter = 3
    fib4 = 0
    index = 0
    while counter < n:
        signature.append(signature[index] +
                         signature[index + 1] + signature[index + 2])
        index += 1
        counter += 1
    return(signature)


print(tribonacci([1, 1, 1], 10))
