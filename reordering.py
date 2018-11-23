text = 'kiran ming Yao'
print(text)


def reorder(text):
    text = text.split()
    for word in text:
        if word[0].isupper():
            text.remove(word)
            text = word + ' ' + ' '.join(text)
            return text


print(reorder(text))
