def next_smaller(n):
    s = list(map(int, list(str(n))))
    count = len(s) - 1
    start = count - 1
    tracker = s[count]
    l = []
    while(count > 0):
        tracker = s[count]
        for i in range(start, -1, -1):
            if s[i] > s[count]:
                s[i], s[count] = s[count], s[i]
                val = ''.join(list(map(str, s)))
                if int(val) < n:
                    return(val)
        start -= 1
        count -= 1

    s = list(map(str, s))


print(next_smaller(531))
print(next_smaller(1234567908))
