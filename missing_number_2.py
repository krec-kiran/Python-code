def missing(s):
    count = int(len(s) / 2)
    start = 0
    end = count
    current = s[start:end]
    digit = int(current)
    next = s[start + count:end + count]
    seq = 0
    while count > 0:
        while end < len(s) - 1 and digit + 1 == int(next):
            seq = True
            if len(str(digit)) > count:
                count += 1
            start += count
            end += count
            current = s[start:end]
            digit += 1
            next = s[start + count:end + count]
        if next and digit + 1 != int(next) and seq:
            return(digit + 1)
        if not next:
            return -1
        count -= 1
        start = 0
        end = count
        current = s[start:end]
        digit = int(current)
        next = s[start + count:end + count]


print(missing('123567'))
print(missing('899091939495'))
print(missing('9899101102'))
print(missing('599600601602'))
