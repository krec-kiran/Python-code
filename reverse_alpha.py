s = 'Hello123Kiran'


def reverse_letter(string):
    s = ''
    for x in string:
        if x.isalpha():
            s += x
    return(s[::-1])


print(reverse_letter(s))
