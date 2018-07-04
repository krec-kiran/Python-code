letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
           'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

s = 'what time are we climbing up the volcano'
s = s.split()


def high(my_list):
    values = []
    count = 0
    index = 0

    for i in s:
        index += 1
        for j in i:
            if j != ' ':
                count += letters[j]
        values.append(count)
        count = 0
    return(s[values.index(max(values))])


print(high(s))
