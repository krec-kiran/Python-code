def pig_latin(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if not s.isalpha():
        return
    s = s.lower()
    if s[0] in vowels:
        result = s + 'way'
    else:
        i = 1
        while i < len(s) - 1 and s[i] not in vowels:
            i += 1
        if s[i] in vowels:
            result = s[i:] + s[:i] + 'ay'
        elif i + 1 == len(s):
            result = s + 'ay'
    return result


print(pig_latin('spaggheti'))
