import collections
def revrot(digits, sz):
    start = 0
    end = 0
    toto = 0
    str1 = ""

    if sz <= 0 or digits is None or sz > len(digits):
        return ""
    while end < len(digits):
        end += sz
        number = digits[start:end]
        start = end
        toto = 0
        for i in number:
            toto = toto + int(i)**3
        if (toto % 2 == 0):
            revo = "".join(reversed(str(number)))
            str1 += revo
        else:
            d = collections.deque(str(number))
            d.rotate(-1)
            str1 = str1 + ''.join(list(d))
        if end + sz > len(digits):
            break
    return(str1)

print(revrot("1234", 0))
print(revrot("1234567893245976", 4))
