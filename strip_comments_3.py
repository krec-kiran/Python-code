# text = 'lemons\napples\noranges cherries strawberries ? cherries\n, watermelons cherries\nwatermelons cherries lemons strawberries watermelons watermelons'

text = ',\nlemons lemons\napples bananas strawberries avocados apples cherries\noranges lemons ! pears cherries pears'
markers = ['!', '^', ',', '@', '.', '-']

print("Slice", text[1:])


def solution(text, markers):
    text = list(text)
    result = ''

    # for i in range(len(text)):
    i = 0
    while i < len(text):
        if len(list(set(text) & set(markers))) == 0:
            print('breakkkkk')
            break

        if i < len(text) and text[i] in markers:
            start = i
            while text[i] != '\n' and i < len(text) - 1:
                i += 1
            before = text[:start]
            if text[i] != '\n':
                after = text[i + 1:]
            elif start == 0:
                before = ''
                after = text[i:]
            else:
                before = text[:start - 1]
                after = text[i:]
            result += ''.join(before)
            result = result.strip()
            # text = list(result)
            print("Current Result", result)
            text = after
            print("TEXT", ''.join(text))
            l = list(set(text) & set(markers))
            print("L IS", l)
            i = - 1
        i = i + 1

    final = ''.join(text)
    final = final.rstrip()
    return(final)


print(solution(text, markers))
#
# '\nlemons lemons\napples bananas strawberries avocados apples cherries\noranges lemons'
#
# ',\nlemons lemons\napples bananas strawberries avocados apples cherries\noranges lemons\nlemons lemons\napples bananas strawberries avocados apples cherries\noranges lemons ! pears cherries pears'
