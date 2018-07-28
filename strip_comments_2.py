text = "watermelons = strawberries\nKiran!\nwatermelons"
text = 'apples, pears \xc2\xa7 and bananas\ngrapes\navocado *apples'
# '\nwatermelons apples watermelons\n\nwatermelons pears'
#
# '#\nwatermelons apples watermelons\n!\nwatermelons pear\nwatermelons apples watermelons'
text = list(text)
markers = ['!', '.', '?', '^', "'", '#', '=', ',', '-']

markers = ['*', '\xc2\xa7']
result = ''
# print(text)

after = text
while (len(after) > 0):
    if len(list(set(after) & set(markers))) == 0:
        break
    for i in range(len(text)):
        print("i now is:", i)
        if i < len(text) and text[i] in markers:
            start = i
            while text[i] != '\n' and i < len(text) - 1:
                i += 1
            print("i is:", i)
            before = text[:start]
            print("Before", ''.join(before))
            if text[i] != '\n':
                after = text[i + 1:]
            else:
                before = text[:start]
                after = text[i:]
                print("Before and After", before, after)

            print("After", ''.join(after))
            result += ''.join(before)
            print("Text now", result)
            text = list(after)
            print(text)

final = ''.join(result)
final = final.strip()
print("Final:\n", final)
