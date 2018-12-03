def cut_fruits(fruits):
    # FRUIT_NAMES is preloded
    FRUIT_NAMES = ['apple', 'pear']
    result = []
    for fruit in fruits:
        if fruit in FRUIT_NAMES:
            if len(fruit) % 2 != 0:
                limit = int((len(fruit) + 1) / 2)
                result.append(fruit[:limit])
                result.append(fruit[limit:])
            else:
                limit = int(len(fruit) / 2)
                result.append(fruit[:limit])
                result.append(fruit[limit:])
        else:
            result.append(fruit)
    return result


print(cut_fruits(["apple", "pear", "bomb"]))
