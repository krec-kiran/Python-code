def remove_every_other(my_list):
    new_list = []
    for item in range(len(my_list)):
        if item % 2 == 0:
            new_list.append(my_list[item])
    return new_list


def remove_every_other_2(my_list):
    return [item for item in my_list if my_list.index(item) % 2 == 0]


print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(remove_every_other_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
