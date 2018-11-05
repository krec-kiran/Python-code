def seven(m):
    m = [int(x) for x in str(m)]
    count = 0
    val = 0
    while len(m) > 2:
        first = m[:-1]
        last = m[-1:]
        count += 1
        first_val = int(''.join(str(x) for x in first))
        last_val = int(''.join(str(x) for x in last))
        val = first_val - 2 * last_val
        m = val
        if m < 0:
            break
        if m >= 0:
            m = [int(x) for x in str(m)]
    return((val, count))


print(seven(1369851))
