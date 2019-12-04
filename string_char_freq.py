def string_char_freq(string):
    chars = set(string)
    char_counter = dict()
    for char in chars:
        char_counter[char] = string.count(char)
    print(char_counter)
    print(max(set(char_counter.values())))
    print(min(set(char_counter.values())))

    if len(set(char_counter.keys())) > 1:
        # diff = max(set(char_counter.values())) - \
        #     min(set(char_counter.values()))
        if min(set(char_counter.values())) == 1:
            return True
        if diff == 1:
            return True
        if set(char_counter.values()) == {1}:
            return True
    if len(set(char_counter.keys())) == 1:
        return True

    return False


print(string_char_freq('hhehhh'))
