def wave(s):
    l = []
    for i in range(len(s)):
        if s[i] != ' ':
            l.append(s[:i] + s[i].upper() + s[i + 1:])
    return l


print(wave('two words'))
