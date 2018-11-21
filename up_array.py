arr = [2, 9, 9, 9]


def up_array(arr):
    if len(arr) <= 0:
        return None
    if len(list(filter((lambda x: x < 0), arr))) > 0:
        return None
    if len(list(filter((lambda x: x > 9), arr))) > 0:
        return None
    arr = [str(x) for x in arr]
    k = ''.join((arr))
    k = int(k) + 1
    return([int(x) for x in str(k)])


print(up_array(arr))
