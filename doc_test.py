import json

set_list = []
with open("doc1.txt") as f:
    l1 = list(set(f.read().split()))
    set_list.append(l1)
    # print(l1)

with open("doc2.txt") as f:
    l2 = list(set(f.read().split()))
    set_list.append(l2)

    # print(l2)

with open("doc3.txt") as f:
    l2 = list(set(f.read().split()))
    set_list.append(l2)


def create_sets(filename):
    with open("doc2.txt") as f:
        l1 = list(set(f.read().split()))
        set_list.append(l1)


print("The intersection is...")
k = set(l1).intersection(set(l2))
common_elements = set(k)


file_names = ["doc1.txt", "doc2.txt", "doc3.txt"]

common_elements = set.intersection(*map(set, set_list))
print(common_elements)
# common_elements = set()

# def find_common_elements():
#     for fp in file_names:
#         create_sets(fp)
#     common_elements = set.intersection(*map(set, set_list))
#     print(common_elements)


# find_common_elements()

word_dict = {}

doc_dict = {}

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
                # print("\nWORD:", word, "\tfilename",file_name, "\n\nLINE:", x)
                break
        temp[file_name] = x
    word_dict[word] = temp
print("NEW DOC DICTIONARY...........")

test = json.dumps(word_dict)
print(test)

# Build following dictionary of words as keys to a dictionary with text file as key and
# lines as values - basically dictionary of dictionary!

# {'word':{ 'doc1.txt':'doc1.txt word sentence','doc2.txt':'doc2.txt word sentence'} }
