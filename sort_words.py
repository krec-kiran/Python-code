words = input("Enter the word list seperated by commas...\n")

# print(word_list) - split outputs a list using comma as seperator

word_list = words.split(',')

# sorted(listname) is the function to sort a list alphabetically

sorted_items = sorted(word_list)

# ','.join() to concatenate string with comma seperated words.

sorted_items = ','.join(sorted_items)

print("Alphabetical sorted word list...\n",sorted_items)

