s = 'Lets all go on holiday somewhere very cold'


def find_short(s):
    string = s.split()
    shortest = len(string[0])
    for i in range(len(string)):
        if len(string[i]) < shortest:
            shortest = len(string[i])

    return(shortest)


print(find_short(s))
