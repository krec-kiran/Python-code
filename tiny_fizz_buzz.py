def tiny_fizz_buzz(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new_string = ''
    for character in string:
        if character not in vowels:
            if character.isupper():
                new_string += 'Iron'
            elif character.islower() or not character.isalpha():
                new_string += character
        else:
            if character.isupper():
                new_string += 'Iron Yard'
            else:
                new_string += 'Yard'
    return new_string


# print(tiny_fizz_buzz('Hello WORLD!'))
