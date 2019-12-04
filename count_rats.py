
def count_rats(town):
    town = town.replace(' ', '').strip()
    rats = town.split('P')
    rat_left = list(rats[0])
    rat_right = list(rats[1])
    return find_deaf_rats(rat_left, 'O~') + find_deaf_rats(rat_right, '~O')


def find_deaf_rats(rat_list, type):
    deaf_rats = 0
    for index in range(0, len(rat_list), 2):
        item = rat_list[index:index + 2]
        if ''.join(item) == type:
            deaf_rats += 1
    return deaf_rats


print(count_rats('~O~O~O~O P'))
print(count_rats('P O~ O~ ~O O~'))
print(count_rats('~O~O~O~OP~O~OO~'))
