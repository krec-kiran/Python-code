from collections import defaultdict


def read_file_contents(file_pointer):
    char_counter = defaultdict(int)
    with open(file_pointer, 'r') as file:
        for line in file:
            for char in line:
                char_counter[char] += 1

    return((sorted(char_counter.items(), key=lambda element_sort_by: element_sort_by[1])))


print(read_file_contents('count_rats.py'))
