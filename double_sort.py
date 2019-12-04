
def double_sort(arr):
    words_list = []
    numbers_list = []
    for item in arr:
        if isinstance(item, int):
            numbers_list.append(item)
        else:
            words_list.append(item)
    return (sorted(numbers_list) + sorted(words_list))


print(double_sort(["Banana", "Orange", "Apple", "Mango", 0, 2, 2]))
print(double_sort(['come', 'on', 110, '2500', 10, '!', 7, 15, 5, 6, 6]))
