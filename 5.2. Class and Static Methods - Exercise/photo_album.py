from math import ceil


class PhotoAlbum:
    PAGE_LIMIT = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = self.build_photos()

    def build_photos(self):
        result = []
        for _ in range(self.pages):
            result.append([])
        return result

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PAGE_LIMIT)
        return cls(pages)

    def add_photo(self, label: str):
        for row, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PAGE_LIMIT:
                page.append(label)
                return f"{label} photo added successfully on page {row + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        delimiter = 11 * "-"
        result = delimiter + '\n'

        for page in self.photos:
            page_str = ' '.join(['[]' for _ in page])
            result += page_str + '\n' + delimiter + '\n'

        return result.strip()