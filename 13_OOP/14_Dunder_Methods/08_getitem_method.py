# Program: __getitem__() Dunder Method
# Description: Demonstrates how __getitem__() allows a custom object
# to access items using the square bracket [] operator.

class Playlist:

    def __init__(self, songs):
        self.songs = songs

    def __getitem__(self, index):
        return self.songs[index]

playlist = Playlist(["Song A", "Song B", "Song C", "Song D"])

song1 = playlist[0]
song2 = playlist[1]

print(song1, song2)
