text = ',\nlemons lemons\napples bananas strawberries avocados apples cherries\noranges lemons ! pears cherries pears'
markers = ['!', '^', ',', '@', '.', '-']


def solution(text, markers):
    print("Text", text)
    print("Markers", markers)
    text = list(text)

    i = 0
    while i < len(text):
        if i < len(text) and text[i] in markers:
            start = i
            while text[i] != '\n' and i < len(text) - 1:
                i += 1
            before = text[:start]
            if text[i] != '\n':
                after = text[i + 1:]
            elif start == 0:
                before = []
                after = text[i:]
            else:
                before = text[:start - 1]
                after = text[i:]
            result = ''.join(before + after)
            result = result.strip()
            text = list(result)
        l = list(set(text) & set(markers))
        print(l)
        if len(l) == 0:
            break
        i += 1
    final = ''.join(text)
    final = final.rstrip()
    return(final)


print(solution(text, markers))
