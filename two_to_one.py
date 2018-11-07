s1 = 'aretheyhere'
s2 = 'yestheyarehere'


def longest(s1, s2):
    return(''.join(sorted(set(s1 + s2))))


print(longest(s1, s2))
