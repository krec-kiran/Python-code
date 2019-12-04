import json
from itertools import combinations

set_list = []
word_dict = {}
doc_dict = {}


def find_combos():
    f_names = ["doc1.txt", "doc2.txt", "doc3.txt", 'doc4.txt', 'doc5.txt']
    combo_list = []
    for x in range(2, len(f_names) + 1):
        comb = combinations(f_names, x)
        for i in list(comb):
            combo_list.append(i)
    return combo_list


def create_sets(filename):
    with open(filename) as fp:
        l1 = list(set(fp.read().split()))
        set_list.append(l1)


def find_common_elements(possibilities):
    for fp in possibilities:
        create_sets(fp)
    shared_elements = set.intersection(*map(set, set_list))
    return shared_elements


def doc_parser():
    possibilities = find_combos()
    for combination in possibilities:
        common_elements = find_common_elements(list(combination))
        for word in common_elements:
            temp = {}
            for file_name in combination:
                temp_list = []
                f = open(file_name, "r")
                f1 = f.readlines()
                txt = ''.join(f1)
                txt.split('.')
                p = [x for x in map(str.strip, txt.split('.')) if x]
                for x in p:
                    if word in x:
                        temp_list.append(x)
                temp[file_name] = temp_list

            word_dict[word] = temp

        test = json.dumps(word_dict)
    print("DOC PARSER OUTPUT\n")
    print(test)


doc_parser()
