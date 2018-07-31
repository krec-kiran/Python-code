l = [[3, 2], [4], []]


def elements_sum(arr, d=0):
    sum = 0
    index = len(arr) - 1
    print(index)
    for i in arr:
        if i and len(i) > index:
            sum += i[index]
            index -= 1
            print(sum)
        elif len(i) <= index:
            if d:
                sum += d
            else:
                sum += 0
            index -= 1
    return sum


print(elements_sum([[3, 2], [4], []]))
