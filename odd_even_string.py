def sort_my_string(s):
    even = ''
    odd = ''
    for i in range(len(s)):
        if i % 2 == 0:
            even += s[i]
        else:
            odd += s[i]

    return(even + ' ' + odd)


print(sort_my_string("CodeWars"))
