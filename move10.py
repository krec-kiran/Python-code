def move_ten(st):
    result = ''
    for i in st:
        val = ord(i) + 10
        if val > 122:
            result += chr(ord('a') + (val) - 123)
        else:
            result += chr(ord(i) + 10)
    return(result)


print(move_ten('testcase'))
print(move_ten('codewars'))
