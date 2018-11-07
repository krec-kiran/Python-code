arr = [9, 3]


def explode(arr):
    if str(arr[0]).isdigit() and str(arr[1]).isdigit():
        return([arr] * (arr[0] + arr[1]))
    if str(arr[0]).isdigit():
        return([arr] * arr[0])
    if str(arr[1]).isdigit():
        return([arr] * arr[1])
    else:
        return('Void!')


print(explode(arr))
