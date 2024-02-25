from project.song import Song


class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.published = False
        self.songs = [x for x in args]

    def add_song(self, song: Song):
        if song in self.songs:
            return "Song is already in the album."

        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return f"Cannot add songs. Album is published."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."

        for given_song in self.songs:
            if given_song.name == song_name:
                self.songs.remove(given_song)
                return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):
        return f"Album {self.name}\n" + "\n".join([f"== {x.get_info()}" for x in self.songs])
