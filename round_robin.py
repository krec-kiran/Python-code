def roundRobin(jobs, time, index):
    total = 0
    i = -1
    while jobs[index] > 0:
        if i < len(jobs) - 1:
            i += 1
        else:
            i = 0
        if jobs[i] - time > 0:
            jobs[i] = jobs[i] - time
            total += time
        elif jobs[i] - time <= 0 and jobs[i] > 0:
            total += jobs[i]
            jobs[i] = 0
        if jobs[index] == 0:
            break
    return(total)


print(roundRobin([10, 20, 1], 5, 0))
