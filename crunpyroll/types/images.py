from ..enums import ImageType

from .obj import Object

from typing import List, Dict

class Images(Object):
    def __init__(self, data: Dict):
        self.poster_tall: List["Image"] = Image.from_list(data.get("poster_tall"))
        self.poster_wide: List["Image"] = Image.from_list(data.get("poster_wide"))
        self.promo_image: List["Image"] = Image.from_list(data.get("promo_image"))
        self.thumbnail: List["Image"] = Image.from_list(data.get("thumbnail"))

class Image(Object):
    def __init__(self, data: Dict):
        self.width: str = data.get("width")
        self.height: int = data.get("height")
        self.url: str = data.get("source")
        self.type: "ImageType" = ImageType(data.get("type"))

    @classmethod
    def from_list(cls, lst: List) -> List:
        if lst:
            return [
                Image(image) for obj
                in lst for image in obj
            ]