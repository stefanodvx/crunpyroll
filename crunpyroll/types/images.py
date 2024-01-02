from ..enums import ImageType

from .obj import Object

class Images(Object):
    def __init__(self, data: dict):
        self.poster_tall: list["Image"] = Image.from_list(data.get("poster_tall"))
        self.poster_wide: list["Image"] = Image.from_list(data.get("poster_wide"))
        self.promo_image: list["Image"] = Image.from_list(data.get("promo_image"))
        self.thumbnail: list["Image"] = Image.from_list(data.get("thumbnail"))

class Image(Object):
    def __init__(self, data: dict):
        self.width: str = data.get("width")
        self.height: int = data.get("height")
        self.url: str = data.get("source")
        self.type: "ImageType" = ImageType(data.get("type"))

    @classmethod
    def from_list(cls, lst):
        if lst:
            return [
                Image(image) for obj
                in lst for image in obj
            ]