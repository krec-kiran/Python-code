class Music():

    def __init__(self):
        self.songs = []

    def addtrack(self, artist, track):
        self.artist = artist
        self.songs.append(track)

    def getSongs(self):
        i = 0
        print("The songs of artist {0}".format(self.artist))
        while i < len(self.songs):
            print(self.songs[i])
            i = i + 1
