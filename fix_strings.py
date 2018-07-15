s = 'coDe waRs'


def solve(s):
    upper = [x for x in s if x.isupper()]
    lower = [x for x in s if x.islower()]
    if len(upper) > len(lower):
        s = s.upper()
    else:
        s = s.lower()
    return(s)


print(solve(s))
