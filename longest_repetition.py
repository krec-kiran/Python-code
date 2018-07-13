def longest_repetition(string):
    s = u"%s" % (string)
    longest = 1
    current_longest = 1
    if len(s) == 0:
        return(('', 0))
    else:
        current_letter = s[0]
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            letter = s[i]
            longest += 1
            if longest > current_longest:
                current_longest = longest
                current_letter = s[i]
        else:
            longest = 1
    return((current_letter, current_longest))


print(longest_repetition('aaabbbbcedkkkkkklmnfff'))
