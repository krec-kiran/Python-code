with open("music-albums.txt") as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    i = 0
    music = dict()
    albums = dict()
    line = []
    fans = []

    while i < len(content):
        line = content[i].split(':', 1)
        line[0] = line[0].strip()
        fans.append(line[0])
        line[1] = (line[1].strip()).split(',', 10)
        music.setdefault(line[0], [])
        if line[0] in music:
            music[line[0]].append(line[1])
        else:
            music[line[0]] = line[1]
        i = i + 1

mydict = dict()

sorted_items = dict()

# print(fans)

alb = []
for k, v in music.items():
    alb.append(v)

print("ALBUM",alb)


# result = [ x ** y for x in [10, 20, 30] for y in [2, 3, 4]]
alb = [x for sublist in alb for item in sublist for x in item]
print("FIRST ALB",alb)


mylist = list(set(alb))

for value in mylist:
    for k, v in music.items():
        for item in v:
            for x in item:
                mydict.setdefault(x, [])
                if value == x:
                    mydict[value].append(k)

# print("MyDict..",mydict)

# print("\n")

# for item in mydict.items():
#     print(len(item[1]))

# print("MYDICT",mydict)
sorted_items = sorted(mydict.items(), key = lambda item_length : len(item[1]),reverse=True)
# sorted_items.reverse()
print("\nSorted Items\n",sorted_items)

ans=[]
update=[]

for k,v in sorted_items:
    if not set(v).issubset(update):
            ans.append(k)
    update = update + v
    fans=list(set(fans) - set(v))

print("\nHappy employees bands\n",ans)
