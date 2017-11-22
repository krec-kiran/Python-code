words = input("Enter the word list seperated by commas...\n")

word_list = words.split(',')

# print(word_list) - split outputs a list using comma as seperator

sorted_items = sorted(word_list)

# ','.join() to concatenate string with comma seperated words.

sorted_items = ','.join(sorted_items)

print("Alphabetical sorted word list...\n",sorted_items)

