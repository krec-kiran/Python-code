def encode(message, key):
    l = list(map(chr, range(97, 123)))
    d = dict()

    k = 1
    for i in l:
        d[i] = k
        k += 1

    code = []
    for i in message:
        code.append(d[i])

    key = str(key)
    k = 0
    for i in range(len(code)):
        if k == len(key):
            k = 0
        code[i] += int(key[k])
        k += 1
    return(code)


print(encode("masterpiece", 1939))
print(encode("scout", 1939))
