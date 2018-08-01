myl = [(1, 2), (3, 4), (5, 6)]
interval = (2, 3)

for i in range(len(myl)):
    if set(myl[i]).intersection(set(interval)):
        print(min(zip(myl[i], interval, myl[i + 1])))
        # , max(zip(myl[i], interval, myl[i + 1]))))
