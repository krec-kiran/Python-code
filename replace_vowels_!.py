vowels = 'aeiouAEIOU'
string = 'Hi! Hi!'
for x in string:
    if x in vowels:
        string = string.replace(x, '!')

print(string)
