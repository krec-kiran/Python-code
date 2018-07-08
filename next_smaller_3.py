
from itertools import permutations


def nextSmaller(n):
    l = list(str(n))
    print("L is", l)
    big = '0'
    # print(l)
    # print(last)
    index = 0
    after = []
    before = []
    final = 0
    count = len(l) - 1
    start = count
    print("BEGIN", start)
    while(count >= 0):
        last = l[count]
        print("LAST", last)
        for i in range(count, -1, -1):
            print("i running", l[i])
            if l[i] > last:
                index = i
                print("big", l[i])
                print("prev", l[count])
                l[count], l[i] = l[i], l[count]
                last = l[i]
                print("Final", l)
                # break
            # print("index", index)
            # index += 1
            # print(l[index + 1:])
        print("BEFORE L", l)
        before = l[:index]
        print("BEFORE", before)
        after = sorted(l[index:], reverse=True)
        print("AFTER", after)
        final = ''.join(before) + ''.join(after)
        print("FINAL", final)
        # print("sorted l", l)
        # print("Join", l[:index + 1])
        if(int(final) < n and len(str(int(final))) == len(str(n))):
            return int(final)
        count -= 1
        print("COUNT", count)

    return(-1)


print(nextSmaller(514))
# print(nextSmaller(2071))


# print(nextSmaller(100))

# print(nextSmaller(29009))
# print(nextSmaller(120235849778909360000122334567788999))
# print(nextSmaller(123456798))
# print(nextSmaller(2071))
