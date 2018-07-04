t = ['hay', 'junk', 'needle', 'hay', 'moreJunk', 'randomJunk']


def find_needle(s):
    for word in s:
        if word == 'needle':
            result = 'found the needle at position ' + str(s.index(word))
            return result


print(find_needle(t))
