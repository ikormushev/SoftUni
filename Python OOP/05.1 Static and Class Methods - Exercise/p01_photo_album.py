from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_PER_PAGE))

    def add_photo(self, label: str):
        for page_num in range(len(self.photos)):
            if len(self.photos[page_num]) < self.PHOTOS_PER_PAGE:
                self.photos[page_num].append(label)
                return (f"{label} photo added successfully on page "
                        f"{page_num + 1} slot {len(self.photos[page_num])}")
        return "No more free slots"

    def display(self):
        string_to_return = 11 * "-" + "\n"
        for page_num in range(len(self.photos)):
            if len(self.photos[page_num]) > 0:
                string_to_return += "[] " * (len(self.photos[page_num]) - 1) + "[]"

            string_to_return += "\n" + 11 * "-" + "\n"

        return string_to_return[:-1]
