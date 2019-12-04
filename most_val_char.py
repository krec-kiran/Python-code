def most_val_char(string):
    lex_list = []
    difference = 0
    current_letter = ''
    for pos in range(len(string)):
        position = string.find(string[pos], pos + 1, len(string))
        if position == -1 and string.count(string[pos]) <= 1:
            lex_list.append(string[pos])
        elif string.count(string[pos]) > 1:
            new_difference = position - pos
            print('new_diff',new_difference)
            if new_difference > difference:
                difference = new_difference
                current_letter = string[pos]
                print("DIFF", difference, current_letter)

        print(string[pos], position)
    if difference > 0:
        print("vals", difference,current_letter)
    else:
        lex_list.sort()
        print(lex_list, lex_list[0])


print(most_val_char("aabccc"))
