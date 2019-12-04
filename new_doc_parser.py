import json
from itertools import combinations


set_list = []
file_names = ["doc1.txt", "doc2.txt", "doc3.txt"]
word_dict = {}
doc_dict = {}


def find_combos():
    f_names = ["doc1.txt", "doc2.txt", "doc3.txt"]
    combo_list=[]

    for x in range(2,len(f_names)+1):
        comb = combinations(f_names, x)
        for i in list(comb):
            combo_list.append(i)
    return combo_list


def create_sets(filename):
    with open(filename) as fp:
        l1 = list(set(fp.read().split()))
        set_list.append(l1)
        print(set_list)


def find_common_elements(possibilities):
    # possibilities=find_combos()
    # print("POSS",possibilities)
    # for combination in possibilities:
    #     print("combination",combination)
    for fp in possibilities:
        create_sets(fp)
    shared_elements = set.intersection(*map(set, set_list))
    return shared_elements


def doc_parser():
    # possibilities = find_combos()
    # print("POSS", possibilities)
    # common_elements=set()
    # for combination in possibilities:
    #     print("COMBINATION",combination)
    common_elements = find_common_elements(file_names)
    print(common_elements)
    for word in common_elements:
        temp = {}
        for file_name in file_names:
            f = open(file_name, "r")
            f1 = f.readlines()
            txt = ''.join(f1)
            txt.split('.')
            p = [x for x in map(str.strip, txt.split('.')) if x]
            for x in p:
                if word in x:
                    break
            temp[file_name] = x
        word_dict[word] = temp

    print("DOC PARSER OUTPUT\n")
    test = json.dumps(word_dict)
    print(test)
    print(find_combos())


doc_parser()
