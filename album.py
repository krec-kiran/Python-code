with open("music.txt") as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    i = 0
    music = {}
    line = []

    while i < len(content):
        line = content[i].split('-', 1)
        line[0] = line[0].strip()
        line[1] = line[1].strip()
        music[line[0]] = line[1]
        i = i + 1

print("Music Dictionary....", music)
print(music['Pixies'])
