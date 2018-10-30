def high_and_low(numbers):
    numbers = numbers.split()
    numbers = list(map(int, numbers))
    output = ("%s %s" % (max(numbers), min(numbers)))
    return output
