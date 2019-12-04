import os
import json
from itertools import combinations


# get source files from the current working directory

def get_source_files():
    doc_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.txt'):
                doc_list.append(file)
        return doc_list


# find all possible combinations / unique groups of documents

def find_combos():
    doc_titles = get_source_files()
    combo_list = []
    for block_size in range(2, len(doc_titles) + 1):
        combo = combinations(doc_titles, block_size)
        for subset in list(combo):
            combo_list.append(subset)
    return combo_list


# tokenize the lines without duplicates from each file

def create_word_sets(filename):
    with open(filename) as fp:
        word_tokens = list(set(fp.read().replace('.', "").strip('.').split()))
        set_list.append(word_tokens)
        return set_list


# find common elements of the group of sets

def find_common_elements(possibilities):
    for possibility in possibilities:
        create_word_sets(possibility)
    shared_elements = set.intersection(*map(set, set_list))
    return shared_elements


# capture the parser output in json format

def output_json(source):
    parsed_file = open("parser_output.json", "w")
    parsed_file.write(source)
    parsed_file.close()


# main parser module that triggers the processing

def doc_parser():
    possibilities = find_combos()
    for combination in possibilities:
        common_elements = find_common_elements(list(combination))
        for word in common_elements:
            line_extract = {}
            for file_name in combination:
                holding_line_list = []
                file_pointer = open(file_name, "r")
                txt = ''.join(file_pointer.readlines())
                txt.split('.')
                lines = [line for line in map(str.strip, txt.split('.')) if line]
                for line in lines:
                    if word in line.split():
                        holding_line_list.append(line)
                line_extract[file_name] = holding_line_list

            word_dict[word] = line_extract

        parser_output = json.dumps(word_dict)
        output_json(parser_output)


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    set_list = []
    word_dict = {}

    doc_parser()
