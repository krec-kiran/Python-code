numbers = [4, 6, 8, 7, 5]


def pendulum(numbers):
    result = []
    numbers = sorted(numbers)
    result = [numbers[0]]
    numbers = numbers[1:]
    length = len(numbers)

    for i in range(length):
        if i % 2 != 0:
            result = [numbers[i]] + result
        else:
            result = result + [numbers[i]]

    return(result)


print(pendulum(numbers))
