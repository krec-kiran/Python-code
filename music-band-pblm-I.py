from collections import Counter

with open("music-albums.txt") as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    i = 0
    music = dict()
    albums = dict()
    line = []


    while i < len(content):
        line = content[i].split(':', 1)
        line[0] = line[0].strip()
        line[1] = (line[1].strip()).split(',',10)
        music.setdefault(line[0], [])
        if line[0] in music:
            music[line[0]].append(line[1])
        else:
            music[line[0]] = line[1]
        i = i + 1

# print("Music Dictionary....", music)

# 1. Create a list from music dictionray
# 2. Loop through it, as it is dictionary containing lists within list and create a flat list of lists
# - hence duplicate alb statements
# 3. count the number of repitions and make a dictionary out of it
# 4. loop through this dictionary and create a sorted list of tuples
# 5. output the top three using for range combo

alb = []
for k,v in music.items():
    alb.append(v)

alb = [item for sublist in alb for item in sublist]
alb = [item for sublist in alb for item in sublist]


alb = dict(Counter(alb))


items = [(v, k) for k, v in alb.items()]
items.sort()
items.reverse()
items = [(k, v) for v, k in items]

# print(items)

items = [item for sublist in items for item in sublist]



print("\nThe top three popular albums are:\n")

# A bit convoluted way of capturing all the bands having same popularity
# TBD - the case of having more bands - say 3 or more - at the same level at the popularity of 1 or 2

iter_1=1
length=len(items)
for i in range(3):
    print(items[i*2])
    iter_2 = iter_1
    iter_1 = iter_1 + 2
    while((items[iter_1]==items[iter_2]) and iter_1 < (length-2) ):
        print(items[iter_1+1])
        iter_2 = iter_1
        iter_1 = iter_1 + 2

print("\n")
