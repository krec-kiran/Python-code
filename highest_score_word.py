letters = dict()
index = 0
for i in list(map(chr, range(97, 123))):
    letters[i] = index
    index += 1

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
