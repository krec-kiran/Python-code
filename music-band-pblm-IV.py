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

# print("Music Dictionary....", music)

# print("Fans list...", fans)

likes = dict()

for i in fans:
    for k in music:
        list1 = music[i][0]
        list2 = music[k][0]
        if k != i:
            list3 = list(set(list1) & set(list2))
            length = len(list3)
        if length>=2 and k != i:
            likes.setdefault(i, [])
            likes[i].append(k)

print("\nCompatibilities..\n", likes)
