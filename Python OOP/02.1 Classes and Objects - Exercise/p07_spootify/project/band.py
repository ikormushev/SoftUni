from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for given_album in self.albums:
            if given_album.name == album_name:
                if given_album.published:
                    return "Album has been published. It cannot be removed."
                else:
                    self.albums.remove(given_album)
                    return f"Album {given_album.name} has been removed."

        return f"Album {album_name} is not found."

    def details(self):
        return f"Band {self.name}\n" + "\n".join([x.details() for x in self.albums])
