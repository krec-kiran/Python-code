k = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]


def largest_sum(arr):
    sum = 0
    l = []
    for i in range(len(arr)):
        sum += arr[i]
        l.append(sum)
        if sum < 0:
            sum = 0
    if not l:
        return 0
    elif max(l) < 0:
        return 0
    else:
        return(max(l))


print(largest_sum(k))
