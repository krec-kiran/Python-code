# s = '199819884756'
#      119989884756
s = '285365'
# 935855753
# 358557539
# s = '806566864046997264'
# s = '209917'
#      65668640468997264
# s = '620560858474000392'
l = list(map(int, (list(s))))
print(l)

if l[0] == min(l):
    first_min_index = 0
    second_min = min(l[1:])
    if l.count(second_min) > 1:
        for k in range(len(l) - 1, 0, -1):
            if l[k] == second_min:
                min_index = k
                print(min_index)
                break
    else:
        min_index = l.index(second_min)
    l.pop(min_index)
    l.insert(1, second_min)
    result = int(''.join(str(x) for x in l))
    if l[first_min_index] == l[min_index]:
        print(result, min_index, first_min_index + 1)
    else:
        print(result, min_index, first_min_index)
else:
    small = min(l[1:])

    if l.count(small) > 1:
        for k in range(len(l) - 1, 0, -1):
            if l[k] == small:
                min_index = k
                break
    else:
        if l[1] == 0:
            print('here')
            for i in range(2, len(l) - 1):
                if l[i] > l[0]:
                    print(l)
                    l.pop(1)
                    print(l)
                    # l.insert(i - 1, l[0])
                    print('here')
                    result = int(''.join(str(x) for x in l))
                    print(result, 0, i - 1)
                    break
        else:
            min_index = l.index(small)
            l.pop(min_index)
            l.insert(0, small)
            result = int(''.join(str(x) for x in l))
            print(result, min_index, 0)
