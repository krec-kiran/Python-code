'''Chef has just found a recipe book, where every dish consists of exactly four ingredients.
He is going to choose some two dishes and prepare them for dinner. Of course,
he likes diversity and wants to know whether the two dishes are similar.

Two dishes are called similar if at least half of their ingredients are the same.
In other words, at least two of four ingredients of the first dish should also be present in the second dish.
The order of ingredients doesn't matter.

Your task is to examine T pairs of dishes.
For each pair, check if the two dishes are similar and print "similar" or "dissimilar" accordingly.'''

# d1=['eggs','sugar','flour','salt']
# d2=['sugar','eggs','milk','flour']

d1 = ['cookies', 'sugar', 'grass', 'lemon']
d2 = ['lemon', 'meat', 'chili', 'wood']

x = set(d1)
y = set(d2)

if (len(x & y) >= 2):
    print("similar")
else:
    print("dissimilar")
