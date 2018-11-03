def closest_sum(ints, num):
    print(ints, num)
    k = [x for x in ints if x < 0]
    if k:
        difference = []
        for i in ints:
            difference.append(abs(num - i))

        total = 0
        count = 0
        while count < 3:
            value = ints[difference.index(min(difference))]
            total += value
            difference.remove(min(difference))
            ints.remove(value)
            count += 1
        return total
    else:
        toto = 0
        count = 0
        while count < 3:
            toto += min(ints)
            ints.remove(min(ints))
            count += 1
        return toto
