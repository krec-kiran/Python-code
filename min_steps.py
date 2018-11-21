def minimum_steps(numbers, value):
    n = sorted(numbers)
    steps = -1
    sum = 0
    for i in n:
        sum += i
        steps += 1
        if sum >= value:
            break
    return steps
