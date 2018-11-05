s = "I really hope it works this time..."


def reverse_alternate(s):
    s = s.split()
    result = ''
    for i in range(len(s)):
        if i % 2 != 0:
            result += s[i][::-1] + ' '
        else:
            result += s[i] + ' '

    return(result.strip())


print(reverse_alternate(s))
