def spin_words(sentence):
    s = sentence.split()
    for i in range(len(s)):
        if len(s[i]) >= 5:
            s[i] = s[i][::-1]
    return(' '.join(s))


print(spin_words('Hey fellow warriors'))
