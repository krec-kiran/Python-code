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

# music = MusicFile('/Users/ynonperek/music.txt')

# print(music.artist('Joy Division').songs)


class MusicFile():
    songs = dict()

    def __init__(self, filename):
        self.filename = filename

    def artist(self, name):
        self.artistName = name


class Artist(MusicFile):
    songs = dict()

    def __init__(self, artistName):
        self.artistName = artistName


test = MusicFile("test.txt")


print(test.artist("demo"))
