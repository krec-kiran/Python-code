def draw_stairs(n):
    result = ''
    blank = ' '
    for i in range(n):
        result += 'I'
        if i < n - 1:
            space = blank * (i + 1)
            result += '\\n' + space
    return result


print(draw_stairs(10))
