s1 = 'coding'
s2 = 'anywhere'

letter = 'n'


def string_merge(string1, string2, letter):
    return string1[:string1.find(letter)] + string2[string2.find(letter):]


print(string_merge(s1, s2, letter))
