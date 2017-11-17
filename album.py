with open("music.txt") as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    i = 0
    music = dict()
    line = []

    while i < len(content):
        line = content[i].split('-', 1)
        line[0] = line[0].strip()
        line[1] = line[1].strip()
        music.setdefault(line[0], [])
        if line[0] in music:
            music[line[0]].append(line[1])
        else:
            music[line[0]] = line[1]
        i = i + 1

print("Music Dictionary....", music)
print(music['Pixies'])
