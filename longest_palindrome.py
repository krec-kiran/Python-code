import re


def longest_palindrome(text):
    text = " ".join(re.findall("[0-9a-zA-Z]+", text))
    text = text.replace(' ', '')
    text = text.lower()
    palindrome_length = 0
    common_char_count = 0
    already_seen = []

    for character in text:
        if character not in already_seen:
            if text.count(character) % 2 == 0:
                already_seen.append(character)
                palindrome_length += text.count(character)
            elif text.count(character) > 1:
                already_seen.append(character)
                palindrome_length += text.count(character) - 1
            elif text.count(character) == 1 and common_char_count == 0:
                common_char_count += 1
                palindrome_length += 1
    if common_char_count <= 1:
        return(palindrome_length)


print(longest_palindrome('$aaabbbccddd_!jJpqlQx_.///yYabababhii_'))
print(longest_palindrome('xyz__a_/b0110//a_zyx'))
print(longest_palindrome('Hannah'))
