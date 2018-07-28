def contain_all_rots(strng, arr):
    if strng == '':
        return True
    l = []
    end = len(strng) - 1
    for i in range(len(strng)):
        before = strng[i:]
        after = strng[:i]
        k = before + after
        l.append(k)
    if set(l).issubset(arr):
        return True
    else:
        return False


print(contain_all_rots("UDvG", ['vGUD', 'UDvG', 'GUDv', 'DvGU']))
