arr = [['gOOd', 'bad', 'BAD', 'bad', 'bad'], [
    'bad', 'bAd', 'bad'], ['GOOD', 'bad', 'bad', 'bAd']]


def well(arr):
    goodness = 0
    for i in range(len(arr)):
        for j in arr[i]:
            if isinstance(j, str) and j.lower() == 'good':
                goodness += 1
    if goodness > 2:
        return('I smell a series!')
    if goodness == 2:
        return('Publish!')
    return('Fail!')


print(well(arr))
