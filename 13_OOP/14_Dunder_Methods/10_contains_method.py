# Program: __contains__() Dunder Method
# Description: Demonstrates how __contains__() allows a custom object
# to support membership testing using the in operator.

class Playlist:

    def __init__(self, songs):
        self.songs = songs

    def __contains__(self, song):
        return song in self.songs

playlist = Playlist(["Song A", "Song B", "Song C"])

print("Song A" in playlist)
print("Song B" in playlist)
print("Song D" in playlist)