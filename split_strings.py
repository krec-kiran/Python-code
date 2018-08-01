s = 'asdfads'


def solution(s):
    start = 0
    end = 2
    l = []
    while end <= len(s):
        l.append(s[start:end])
        start += 2
        end += 2
    if len(s) % 2 != 0:
        l.append(s[start:] + '_')
    return(l)


print(solution(s))
