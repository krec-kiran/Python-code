def password_maker(phrase):
    new_password = ''
    words = phrase.split()
    password_hash = {'I': '1', 'i': '1',
                     'O': '0', 'o': '0', 'S': '5', 's': '5'}
    for letter in words:
        if letter[0] in password_hash.keys():
            new_password += password_hash[letter[0]]
        else:
            new_password += letter[0]
    return new_password


print(password_maker('Hello world India super London'))
