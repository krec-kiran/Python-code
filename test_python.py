# from collections import OrderedDict
#
# lang_dictionary = dict()
#
# lang_dictionary['priya'] = 'ruby'
# lang_dictionary['aryan'] = 'scala'
# lang_dictionary['rishi'] = 'java script'
# lang_dictionary['kiran'] = 'python'
#
# names = ''
# for name, lang in lang_dictionary.items():
#     print(name.title() + "\'s favorite programming language is: " + lang.title())
#     names += name[0]
# print(''.join(names.title()) + ' Tech Consultancy')


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(list(filter(lambda x: x % 3 == 0, l)))
#
# items = [2, 4, 6, 8]
#
#
# def sqr(x):
#     return x * x
#
#
# print(list(map(lambda x: x * x, items)))
#
# from functools import reduce
#
# print(reduce((lambda x, y: x + y), items))

# from itertools import permutations
# string = 'cat'
#
# permutations_list = list(permutations(string))
#
# anagram_list = []
# for item in permutations_list:
#     joined_element = (''.join(item))
#     anagram_list.append(joined_element)
#
#
# print(anagram_list)


# Python function to print permutations of a given list
def permutation(lst):

    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list. remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l


# Driver program to test above function
data = list('cat')
for p in permutation(data):
    print(p)

#
# def double_func(x):
#     temp = []
#     for i in range(x):
#         temp.append(i * 2)
#     return temp
#
#
# for i in double_func(10):
#     print(i)
