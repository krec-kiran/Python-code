def sort_array_by_length(arr):
    words = dict()
    for word in arr:
        words[word] = len(word)
    sorted_words_len_list = sorted(words.items(), key=lambda x: x[1])
    sorted_words_list = [first_element[0]
                         for first_element in sorted_words_len_list]
    return sorted_words_list


print(sort_array_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))
print(sort_array_by_length(["i", "to", "beg", "life"]))
